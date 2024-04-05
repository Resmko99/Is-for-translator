import os.path
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_run.auth.transport.requests import Request

#Настройка скоупа
SCOPES = ['https://www.googleapis.com/auth/drive']
tokenPath = 'token.pickle'
credentialPath = 'credentials.json'   #Путь к файлу 'credentials.json' где лежат данные пользователя

def authenticate():
    creds = None
    if os.path.exists(tokenPath):
        with open(tokenPath, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentialPath, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(tokenPath, 'wb') as token:
            pickle.dump(creds, token)

    drive_service = build('drive', 'v3', credentials=creds)
    return drive_service


def create_folder(drive_service, folder_name):
    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = drive_service.files().create(body=folder_metadata, fields='id').execute()
    return folder.get('id')

def select_folder(drive_service):
    results = drive_service.files().list(q="mimeType='application/vnd.google-apps.folder'",
                                         spaces='drive',
                                         fields='nextPageToken, files(id, name)').execute()
    items = results.get('files', [])
    if not items:
        print('Нет папок.')
    else:
        print('Папки:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))
    folder_id = input("Введите ID папки, в которую хотите загрузить файл: ")
    return folder_id


def upload_file(drive_service, file_path, folder_id, progress_var):
    file_metadata = {
        'name': file_path.split('/')[-1],
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    request = drive_service.files().create(body=file_metadata, media_body=media)
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            progress_var.set(int(status.progress() * 100))


def browse_file():
    file_path = filedialog.askopenfilename()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)


def upload_to_drive():
    file_path = entry_path.get()
    folder_name = entry_folder.get()

    drive_service = authenticate()
    folder_id = create_folder(drive_service, folder_name)
    progress_var.set(0)
    upload_file(drive_service, file_path, folder_id, progress_var)
    progress_var.set(100)


root = tk.Tk()
root.title("Google Drive Upload")

tk.Label(root, text="Выберите файл для загрузки:").pack(pady=5)
entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=5)
tk.Button(root, text="Обзор", command=browse_file).pack(pady=5)

tk.Label(root, text="Введите название папки на Google Диске:").pack(pady=5)
entry_folder = tk.Entry(root, width=50)
entry_folder.pack(pady=5)

tk.Button(root, text="Загрузить на Google Диск", command=upload_to_drive).pack(pady=10)
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, orient="horizontal", mode="determinate")
progress_bar.pack(pady=10)

root.mainloop()


