# 🔒 Secure Model App

This is a Streamlit application template designed to secure your model behind a password protection.

## Features

- **Password Protection**: Uses Streamlit's secrets management to restrict access.
- **Model Placeholder**: Includes a placeholder for your model logic (currently reverses text).

## How to Run Locally

1. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Secrets**

   Create a file at `.streamlit/secrets.toml` with the following content:

   ```toml
   password = "your_secret_password"
   ```

3. **Run the App**

   ```bash
   streamlit run streamlit_app.py
   ```

## Deployment on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Log in to [share.streamlit.io](https://share.streamlit.io/).
3. Click "New app" and select this repository.
4. **Important**: Before deploying (or in the App Settings after deploying), go to the "Secrets" section.
5. Add your password secret in the TOML format:

   ```toml
   password = "your_secure_password_here"
   ```

6. Click "Save" and your app will be secured!

## Customizing the Model

To integrate your actual model:
1. Open `streamlit_app.py`.
2. Locate the `if check_password():` block.
3. Replace the placeholder logic with your model inference code.
