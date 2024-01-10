 # UPSpoken : Bridging the Communication Gap with Real-Time Sign Language Translation
-- Under Development

## Files
[Data-Collection.py](Data-Collection.py)
[Model-Training.md](Model-Training.md)
[Testing.py](Testing.py)
[Resources.md](Resources.md)
[Rough.txt](Rough.txt)

## Team
- [BhatiRishabh](https://github.com/BhatiRishabh/)
- [kintsugi-programmer](https://github.com/kintsugi-programmer)

## Problem

* Deaf individuals often face significant communication barriers with non-deaf people due to the limited understanding of American Sign Language (ASL).
* Current methods, such as typing on mobile devices or using separate speech-to-text apps, are slow and cumbersome.

## Solution

We propose a two-pronged solution:

1. **Real-time sign language detection and translation:**
   - Leverages OpenCV for hand sign recognition.
   - Employs a machine learning model trained with Google Teachable Machine.
   - Converts hand signs to text and simultaneously speaks the text aloud.

2. **Speech-to-enlarged-text:**
   - Detects spoken words and displays them in enlarged text for clear visual communication.

## Product

* **Smartwatch:** Embedded with a camera for seamless sign language translation without additional devices.
* **Mobile app:** Designed for mass accessibility, affordability, and availability.

## Why Us

* **Addresses a critical unmet need:** Existing solutions like Google's Live Transcribe and text-to-speech glasses are limited in functionality and often expensive.
* **Unique real-time translation:** Offers a more comprehensive and accurate approach to sign language communication.
* **Innovative product design:** Explores the potential of wearable technology for direct translation on a smartwatch.
* **Potential for further advancements:** Lays the groundwork for integration with IOT, gesture control, and other innovative applications.

## Development Process

1. **Hand sign detection using OpenCV:**
   - Implement hand and finger tracking algorithms.
   - Extract relevant features for sign recognition.

2. **Model training with Google Teachable Machine:**
   - Collect and label a diverse dataset of ASL signs.
   - Train a machine learning model to recognize signs and map them to corresponding text.

3. **Interface development:**
   - Design an intuitive and user-friendly interface for both smartwatch and mobile app.
   - Integrate text-to-speech and speech-to-text functionalities.

## Screenshots


![Screenshot 1](/images/1.jpeg)
![Screenshot 2](/images/2.jpeg)
![Screenshot 3](/images/3.jpeg)
![Screenshot 4](/images/4.jpeg)

## Future Directions

* **Continuous model improvement:** Gather more data and refine model accuracy.
* **Explore additional features:**
   - Expand translation capabilities to other sign languages.
   - Integrate with voice assistants for enhanced interactions.
   - Customize settings for individual preferences and communication styles.

## Contribute

We welcome contributions and collaborations to further enhance this project and its impact on the deaf community.

## License

UPSpoken is licensed under the MIT License. See the `LICENSE` file for details.

