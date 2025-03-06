# FLAMES Game using Streamlit

This is a simple FLAMES game implemented using Streamlit. The FLAMES game is a fun way to predict the relationship between two people based on their names.

## Features
- Takes two names as input
- Removes common letters and counts the remaining ones
- Uses the FLAMES algorithm to determine the relationship type
- Displays the result interactively using Streamlit

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/flames-game.git
   cd flames-game
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install streamlit
   ```

## Running the App

Run the Streamlit application using:
```sh
streamlit run flames.py
```

## How It Works

1. The user enters two names.
2. Common letters between the two names are removed.
3. The remaining letters are counted and used to cycle through "FLAMES".
4. The final letter represents the relationship:
   - **F** - Friends
   - **L** - Love
   - **A** - Affection
   - **M** - Marriage
   - **E** - Enemy
   - **S** - Sibling
5. The result is displayed interactively using Streamlit.

## Contributing
Feel free to contribute by submitting issues or pull requests!

## License
This project is licensed under the MIT License.

