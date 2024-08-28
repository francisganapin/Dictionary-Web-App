const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    resizable: false,
    autoHideMenuBar: true,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  // Load the URL of your Django app or any URL you want
  mainWindow.loadURL('http://127.0.0.1:8000/');

  // Optionally open DevTools
  // mainWindow.webContents.openDevTools();
}

app.on('ready', () => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

