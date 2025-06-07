# Google OAuth Setup Guide

This guide will help you set up Google Sign-In for your Todo application.

## 🚀 Quick Setup Steps

### 1. Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the **Google+ API** or **Google Identity Services**

### 2. Configure OAuth Consent Screen

1. Go to **APIs & Services** → **OAuth consent screen**
2. Choose **External** user type
3. Fill in required information:
   - **App name**: Todo App
   - **User support email**: Your email
   - **Developer contact email**: Your email
4. Add scopes: `email`, `profile`, `openid`
5. Add test users (your email) for development

### 3. Create OAuth 2.0 Credentials

1. Go to **APIs & Services** → **Credentials**
2. Click **+ CREATE CREDENTIALS** → **OAuth 2.0 Client IDs**
3. Choose **Web application**
4. Configure:
   - **Name**: Todo App Web Client
   - **Authorized JavaScript origins**: 
     - `http://localhost:3000`
     - `http://127.0.0.1:3000`
   - **Authorized redirect URIs**: 
     - `http://localhost:3000`
     - `http://127.0.0.1:3000`

### 4. Get Your Client ID

1. After creating credentials, copy the **Client ID**
2. It should look like: `123456789-abcdef.apps.googleusercontent.com`

### 5. Configure Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` file and replace the Google Client ID:
   ```env
   GOOGLE_CLIENT_ID=your-actual-client-id-here.apps.googleusercontent.com
   NEXT_PUBLIC_GOOGLE_CLIENT_ID=your-actual-client-id-here.apps.googleusercontent.com
   ```

### 6. Restart Your Application

1. Stop the backend server (Ctrl+C)
2. Restart it:
   ```bash
   python run_backend.py
   ```

3. The frontend should automatically pick up the new environment variables

## 🧪 Testing Google Sign-In

1. Go to `http://localhost:3000/login`
2. You should see a "Sign in with Google" button
3. Click it and sign in with your Google account
4. You should be redirected to the todo dashboard

## 🔧 Troubleshooting

### Common Issues:

1. **"Error 400: redirect_uri_mismatch"**
   - Make sure your redirect URIs in Google Console match exactly
   - Include both `http://localhost:3000` and `http://127.0.0.1:3000`

2. **"This app isn't verified"**
   - This is normal for development
   - Click "Advanced" → "Go to Todo App (unsafe)"

3. **"Invalid client ID"**
   - Check that your Client ID is correctly set in `.env`
   - Make sure there are no extra spaces or quotes

4. **Google button doesn't appear**
   - Check browser console for JavaScript errors
   - Ensure the Google Client ID environment variable is set

### Debug Steps:

1. Check browser console for errors
2. Verify environment variables are loaded
3. Test the `/auth/google-login` endpoint in API docs
4. Check backend logs for authentication errors

## 🔒 Security Notes

- Never commit your actual Client ID to version control
- Use different Client IDs for development and production
- Keep your Client Secret secure (not needed for frontend-only OAuth)
- Regularly review OAuth consent screen settings

## 📚 Additional Resources

- [Google Identity Services Documentation](https://developers.google.com/identity/gsi/web)
- [OAuth 2.0 for Web Applications](https://developers.google.com/identity/protocols/oauth2/web-server)
- [Google Cloud Console](https://console.cloud.google.com/)
