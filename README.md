# TAP TAP SONG - Rhythm Game

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Play](#how-to-play)
5. [Game Mechanics](#game-mechanics)
6. [Code Structure](#code-structure)
7. [Dependencies](#dependencies)
8. [License](#license)

---

## Introduction
**TAP TAP SONG** is a rhythm-based game where players must click on objects in sync with the music. The game is built using the **Kivy framework**, which allows for cross-platform development. The goal is to achieve the highest combo by accurately clicking on the objects as they appear on the screen.

---

## Features
- **Rhythm-Based Gameplay**: Click on objects in sync with the music to build your combo.
- **Dynamic Object Movement**: Objects move to different positions on the screen based on the song's sequence.
- **Combo System**: Earn combos by clicking on objects correctly. Miss a click, and the game ends.
- **Interactive Start Screen**: Start the game by pressing the **'R'** key while hovering over the center object.
- **Game Over Screen**: Displays your final combo and allows you to restart the game.

---

## Installation

### Prerequisites
- **Python 3.x**
- **Kivy framework**

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/KIM2548TH/kivy_asiment.git
   cd kivy_asiment
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Game**:
   ```bash
   python main.py
   ```

---

## How to Play

1. **Start the Game**:
   - On the start screen, hover your mouse over the center object and press the **'R'** key to begin the game.

2. **Gameplay**:
   - Objects will appear on the screen at different positions based on the song's sequence.
   - Press the **'D'** key when the object is highlighted to earn a combo.
   - If you miss a click or click at the wrong time, the game will end.

3. **Game Over**:
   - When the game ends, your final combo will be displayed.
   - Press **'R'** to restart the game.

---

## Game Mechanics

- **Object Movement**: Objects move to predefined positions based on the song's sequence. The positions are timed to match the rhythm of the music.
- **Combo System**: Each correct click increases your combo. Missing a click or clicking at the wrong time will end the game.
- **Music Sync**: The game uses a music logic system to sync object movements with the song's beat.

---

## Code Structure

- **main.py**: The main entry point of the game. Initializes the game widget and sets up the game loop.
- **game_widget.py**: Contains the `GameWidget` class, which handles the game logic, object movement, and user input.
- **music_logic.py**: Manages the music playback and syncs the object movements with the song's beat.
- **start.py**: Handles the start screen and initial game setup.
- **main.kv**: The Kivy language file that defines the UI layout and visual elements of the game.

### Key Classes and Methods

- **GameWidget**:
  - `move_object()`: Moves the object to the next position in the song sequence.
  - `on_point()`: Handles user input and checks if the click was correct.
  - `end_game()`: Ends the game and displays the game over screen.

- **MusicLogic**:
  - `start_music()`: Starts playing the music and schedules the object movements.
  - `_on_beat()`: Checks the current time in the song and moves the object accordingly.

- **new_game**:
  - `start_game()`: Resets the game state and initializes the start screen.
  - `reset_game()`: Resets the game variables for a new game.

---

## Dependencies

- **Kivy**: A Python framework for developing multitouch applications.
- **Kivy.clock**: Used for scheduling events and animations.
- **Kivy.core.audio**: Handles music playback.

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

# TAP TAP SONG - เกมกดจังหวะ

## สารบัญ
1. [บทนำ](#บทนำ)
2. [คุณสมบัติ](#คุณสมบัติ)
3. [การติดตั้ง](#การติดตั้ง)
4. [วิธีการเล่น](#วิธีการเล่น)
5. [กลไกของเกม](#กลไกของเกม)
6. [โครงสร้างโค้ด](#โครงสร้างโค้ด)
7. [การพึ่งพา](#การพึ่งพา)
8. [สัญญาอนุญาต](#สัญญาอนุญาต)

---

## บทนำ
**TAP TAP SONG** เป็นเกมที่ใช้จังหวะเพลงเป็นหลัก โดยผู้เล่นต้องคลิกวัตถุให้ตรงกับจังหวะเพลง เกมนี้สร้างขึ้นโดยใช้เฟรมเวิร์ก **Kivy** ซึ่งช่วยให้สามารถพัฒนาเกมข้ามแพลตฟอร์มได้ เป้าหมายคือการทำคอมโบให้ได้สูงสุดโดยการคลิกวัตถุให้ถูกต้องตามเวลาที่กำหนด

---

## คุณสมบัติ
- **เกมเพลย์แบบจังหวะ**: คลิกวัตถุให้ตรงกับจังหวะเพลงเพื่อสร้างคอมโบ
- **การเคลื่อนที่ของวัตถุแบบไดนามิก**: วัตถุจะเคลื่อนที่ไปยังตำแหน่งต่าง ๆ บนหน้าจอตามลำดับของเพลง
- **ระบบคอมโบ**: ได้รับคอมโบเมื่อคลิกวัตถุถูกต้อง หากคลิกผิดหรือพลาดเกมจะจบ
- **หน้าจอเริ่มเกมแบบอินเทอร์แอกทีฟ**: เริ่มเกมโดยการกดปุ่ม **'R'** ขณะที่เมาส์อยู่เหนือวัตถุกลางหน้าจอ
- **หน้าจอจบเกม**: แสดงคอมโบสุดท้ายและอนุญาตให้เริ่มเกมใหม่ได้

---

## การติดตั้ง

### ข้อกำหนดเบื้องต้น
- **Python 3.x**
- **เฟรมเวิร์ก Kivy**

### ขั้นตอน
1. **โคลนรีพอสิทอรี**:
   ```bash
   git clone https://github.com/KIM2548TH/kivy_asiment.git
   cd kivy_asiment
   ```

2. **ติดตั้ง dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **รันเกม**:
   ```bash
   python main.py
   ```

---

## วิธีการเล่น

1. **เริ่มเกม**:
   - บนหน้าจอเริ่มเกม ให้เลื่อนเมาส์ไปเหนือวัตถุกลางหน้าจอและกดปุ่ม **'R'** เพื่อเริ่มเกม

2. **การเล่นเกม**:
   - วัตถุจะปรากฏบนหน้าจอในตำแหน่งต่าง ๆ ตามลำดับของเพลง
   - กดปุ่ม **'D'** เมื่อวัตถุถูกไฮไลต์เพื่อรับคอมโบ
   - หากคลิกผิดหรือพลาดเกมจะจบ

3. **จบเกม**:
   - เมื่อเกมจบ คอมโบสุดท้ายจะแสดงขึ้น
   - กด **'R'** เพื่อเริ่มเกมใหม่

---

## กลไกของเกม

- **การเคลื่อนที่ของวัตถุ**: วัตถุจะเคลื่อนที่ไปยังตำแหน่งที่กำหนดไว้ล่วงหน้าตามลำดับของเพลง โดยตำแหน่งจะถูกกำหนดเวลาให้ตรงกับจังหวะเพลง
- **ระบบคอมโบ**: การคลิกถูกต้องแต่ละครั้งจะเพิ่มคอมโบ หากคลิกผิดหรือพลาดเกมจะจบ
- **การซิงค์เพลง**: เกมใช้ระบบ **Music Logic** เพื่อซิงค์การเคลื่อนที่ของวัตถุกับจังหวะเพลง

---

## โครงสร้างโค้ด

- **main.py**: จุดเริ่มต้นหลักของเกม กำหนดค่าเริ่มต้นของเกมและตั้งค่าการวนลูปเกม
- **game_widget.py**: ประกอบด้วยคลาส `GameWidget` ซึ่งจัดการกับเกมลอจิก การเคลื่อนที่ของวัตถุ และการรับข้อมูลจากผู้เล่น
- **music_logic.py**: จัดการกับการเล่นเพลงและซิงค์การเคลื่อนที่ของวัตถุกับจังหวะเพลง
- **start.py**: จัดการกับหน้าจอเริ่มเกมและการตั้งค่าเริ่มต้นของเกม
- **main.kv**: ไฟล์ภาษา Kivy ที่กำหนดรูปแบบ UI และองค์ประกอบภาพของเกม

### คลาสและเมธอดหลัก

- **GameWidget**:
  - `move_object()`: ย้ายวัตถุไปยังตำแหน่งถัดไปในลำดับเพลง
  - `on_point()`: จัดการการรับข้อมูลจากผู้เล่นและตรวจสอบว่าคลิกถูกต้องหรือไม่
  - `end_game()`: จบเกมและแสดงหน้าจอจบเกม

- **MusicLogic**:
  - `start_music()`: เริ่มเล่นเพลงและกำหนดเวลาการเคลื่อนที่ของวัตถุ
  - `_on_beat()`: ตรวจสอบเวลาปัจจุบันในเพลงและย้ายวัตถุตามจังหวะ

- **new_game**:
  - `start_game()`: รีเซ็ตสถานะเกมและเริ่มต้นหน้าจอเริ่มเกม
  - `reset_game()`: รีเซ็ตตัวแปรเกมสำหรับเกมใหม่

---

## การพึ่งพา

- **Kivy**: เฟรมเวิร์ก Python สำหรับการพัฒนาแอปพลิเคชันแบบมัลติทัช
- **Kivy.clock**: ใช้สำหรับการกำหนดเวลาเหตุการณ์และแอนิเมชัน
- **Kivy.core.audio**: จัดการกับการเล่นเพลง


--- 

สนุกกับการเล่น **TAP TAP SONG**! หากมีคำถามหรือข้อเสนอแนะใด ๆ สามารถเปิด issue หรือมีส่วนร่วมในโปรเจกต์ได้
