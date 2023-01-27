# Pixel Tint 32 x 32 System
This project is an interactive system that teaches us about the physical phenomenon on polarization of lights. Polarisers are controlled by motors to display pixelated images using different angles to create different shades of grey
## Our Feature

# ★Story Telling Show★
Our feature is about a captivating story of a couple's journey together as a pair and taking the viewers with them through their ups and downs during the relationship

<br>

In this generation, many audiences are more drawn to drama and films these days which majority includes romantic genre's. Hence, we want our audiences, teenagers and adults from 13-21 year old to witness our show, and for them to either relate to or just appreciate at the end of it.
<br>

We want to showcase the emotions and feelings of the story through lights and audio, and having the visuals from our very own pixelated images displayed out to the Pixel Tint Panel.
## What our feature consist of:
**Main GUI** 
- Our GUI shows all of the images that will be displayed on the show starting from image 1 to image 16.
- Each image is a button. When button pressed individually **(right frame)**, the image will appear on the blank canvas **(left frame)**, and will send out the image on the polarizer.
![alt text](diagram/Panel.jpg)
*Picture of the Polarizer Panel*
- At the bottom, we have the "Start Show" button which is a command that will automatically send all 16 images in a sequence of 15 seconds delay for each image.
![alt text](diagram/Show_GUI.png)
*Screenshot of our GUI*

<br>

## Components
---
| No. | Equipment |
| ----------- | ----------- |
| 1. | Raspberry Pi 4 |
| 2. |  XLR-M to 3.5mm-M stereo |
| 3. |  **Avolites** Lighting Console |
| 4. |  Mixer - **Model: Yamaha QL1**|
| 5. |  Audio Amplifier - **Model: NXAMP4X2MK2**|
| 6. |  Speakers Line Array and Subwoofers|


## Setup
---
## **Hardware Set Up**

<br>

**Audio Setup:**
<br>

1. Connect Raspberry Pi 4 to a power source
2. Using the XLR-M to a 3.5mm-M stereo cable, from the Raspberry Pi 4 into the mixer (input 1 & 2)
3. Using DANTE to connect up the audio amplifier using CAT6 from primary to primary
4. Using NL4 cables to connect up the speakers from the audio amplifier to the speakers and subwoofers.

![alt text](diagram/audiosetup.jpg)
*Picture of Audio Setup*

**Lighting Setup:**
<br>

The lights are being controlled manually in a console. Hence, it is a separate setup on its own.
<br>

1. In S536, the lights are connected and pre-patched in the console
2. For each image of our story, we created either cues or chases. We used lights such as the 
3. 