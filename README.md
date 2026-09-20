# My first Python web app

Enter your name and click **OK**. The app displays your name in large red letters. The page adapts to different screen widths.

Built with Python and Streamlit as a first programming project.

## Run locally on Windows

Open this folder in VS Code. In its terminal, run:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

The app opens in a browser tab. Press **Ctrl+C** in the terminal to stop it.

## Files

- `app.py` — the form and result.
- `requirements.txt` — the Python dependency used by the app and its online deployment.

## Publish a live demo

1. Create a public GitHub repository named `first-python-web-app`.
2. Upload `app.py`, `requirements.txt` and `README.md` to the repository's main folder.
3. Sign in at [Streamlit Community Cloud](https://share.streamlit.io/) and choose **Create app**. Select the GitHub repository and `app.py` as the entrypoint file.
4. Once the app has a public URL, add that link near the top of this README so visitors can try it.
