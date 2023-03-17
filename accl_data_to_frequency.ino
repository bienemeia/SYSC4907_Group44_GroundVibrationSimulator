#define SAMPLES 256 // number of samples to take for FFT
#define SAMPLING_FREQ 1000 // sampling frequency in Hz
#define ADC_RANGE 1024 // analog-to-digital conversion range
#define VOLTAGE_RANGE 3.3 // voltage range of accelerometer output

const int zPin = A2; // define analog pin for z-axis input

float zRaw; // variable to store raw sensor reading
float zAcc; // variable to store accelerometer reading in g
float zData[SAMPLES]; // array to store accelerometer data for FFT
float zFreq[SAMPLES/2]; // array to store frequency spectrum

void setup() {
  Serial.begin(9600); // initialize serial communication at 9600 bps
}

void loop() {
  // read accelerometer raw data
  zRaw = analogRead(zPin);

  // convert raw data to accelerometer reading in g
  zAcc = ((zRaw / ADC_RANGE) * VOLTAGE_RANGE - VOLTAGE_RANGE/2) / 0.330; // assuming a sensitivity of 330 mV/g for z-axis

  // add accelerometer data to FFT array
  for (int i = 0; i < SAMPLES; i++) {
    zData[i] = zAcc;
  }

  // perform FFT on accelerometer data
  for (int i = 0; i < SAMPLES/2; i++) {
    float real = 0;
    float imag = 0;
    for (int j = 0; j < SAMPLES; j++) {
      float angle = 2 * PI * i * j / SAMPLES;
      real += zData[j] * cos(angle);
      imag -= zData[j] * sin(angle);
    }
    zFreq[i] = sqrt(real * real + imag * imag) / SAMPLES;
  }

  // calculate frequency spectrum
  for (int i = 0; i < SAMPLES/2; i++) {
    zFreq[i] *= 2;
    zFreq[i] /= VOLTAGE_RANGE;
    zFreq[i] /= SAMPLES;
    zFreq[i] *= SAMPLING_FREQ;
  }

  // Print frequency to serial monitor
  Serial.print("Frequency: ");
  for (int i = 0; i < SAMPLES/2; i++) {
      Serial.print("Frequency: ");
      Serial.print(zFreq[0]);
      Serial.println(" Hz");
  }
  Serial.println();
  delay(100); // wait for 1 second before taking the next sample
}
