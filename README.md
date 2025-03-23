# Band Preference Analyzer

## 📌 Overview
The **Band Preference Analyzer** is a Python-based application that processes user-submitted band preferences and analyzes the most liked bands based on user input. It extracts and ranks bands by popularity and lists the users who prefer each band.

## 🎯 Features
- Reads a structured text file containing users and their favorite bands.
- Identifies the **top two most liked bands** based on user preferences.
- Displays a **sorted list of bands along with their respective fans**.

## 🏗️ Project Structure
```
📁 BandPreferenceAnalyzer
│-- 📄 code.py           # Main application script
│-- 📄 inputs.txt        # Input data file containing user preferences
│-- 📄 README.md         # Project documentation
```

## 📥 Input Format
The input file **(inputs.txt)** should be structured as follows:
```
3  # The first line contains the number of user entries
Anne: Metallica, The_Doors, Black_Sabbath
Bob: The_Beatles, Pink_Floyd
Charlie: Nirvana, Metallica
```
- The **first line** specifies the number of user entries.
- Each following line contains a **username**, followed by a **colon (:)**, then a **comma-separated list** of their favorite bands.

## 🚀 How to Run the Application
### **Prerequisites**
- Install **Python 3.x**

### **Steps to Run**
1. **Clone the Repository** (or download the files manually):
   ```sh
   git clone https://github.com/your-repository-url.git
   cd BandPreferenceAnalyzer
   ```
2. **Ensure `inputs.txt` is in the same directory as `code.py`.**
3. **Run the script:**
   ```sh
   python code.py
   ```

## 🛠️ How It Works
1. **`parse_input(file_path)`**: Reads and processes the input file.
2. **`find_top_liked_bands(band_preferences)`**: Identifies the top 2 most liked bands.
3. **`display_band_fans(band_preferences)`**: Displays a sorted list of bands with their respective fans.

## 📤 Expected Output
If `inputs.txt` contains:
```
3
Anne: Metallica, The_Doors, Black_Sabbath
Bob: The_Beatles, Pink_Floyd
Charlie: Nirvana, Metallica
```
The output will be:
```
Metallica

Black_Sabbath: Anne
Metallica: Anne, Charlie
Nirvana: Charlie
Pink_Floyd: Bob
The_Beatles: Bob
The_Doors: Anne
```

## 📌 Notes
- Ensure `inputs.txt` follows the correct format.
- Modify `inputs.txt` to analyze different band preferences.
- The program **ignores malformed lines** that do not contain a colon `:`.