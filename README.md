# Full-Stack Todo Application

A beautiful, modern todo application with Next.js 14 frontend and FastAPI backend. Built with TypeScript, Tailwind CSS, and Python.

## ✨ Features

### 🎨 Frontend (Next.js)
- **Modern UI**: Clean, responsive design with smooth animations
- **Full CRUD Operations**: Create, read, update, and delete todos
- **Smart Filtering**: Filter todos by All, Active, or Completed status
- **Real-time Updates**: Instant UI updates with optimistic rendering
- **TypeScript**: Full type safety throughout the application
- **Responsive Design**: Works perfectly on desktop and mobile devices

### 🚀 Backend (FastAPI)
- **RESTful API**: Complete CRUD operations with OpenAPI documentation
- **Database Integration**: SQLite with SQLAlchemy ORM
- **Data Validation**: Pydantic schemas for request/response validation
- **CORS Support**: Configured for frontend integration
- **Auto-reload**: Development server with hot reload

### 🤖 MCP Server (AI Integration)
- **AI Assistant Access**: Allow AI assistants to manage your todos
- **Model Context Protocol**: Standard interface for AI tool integration
- **Secure Access**: Local database access without network exposure
- **Rich Tool Set**: 11 different tools for comprehensive todo management
- **Real-time Sync**: Changes sync immediately with web application

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ 
- npm, yarn, or pnpm

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   # or
   pnpm install
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.local.example .env.local
   ```
   
   Edit `.env.local` and set your FastAPI backend URL:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   # or
   yarn dev
   # or
   pnpm dev
   ```

4. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 🔧 API Integration

This frontend is designed to work with a FastAPI backend that provides the following endpoints:

- `GET /todos` - Get all todos
- `POST /todos` - Create a new todo
- `PUT /todos/{id}` - Update a todo
- `DELETE /todos/{id}` - Delete a todo

### Expected Todo Data Structure

```typescript
interface Todo {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;
  updated_at?: string;
}
```

## 📁 Project Structure

```
src/
├── app/
│   ├── globals.css          # Global styles
│   ├── layout.tsx           # Root layout
│   └── page.tsx             # Main todo page
├── components/
│   ├── AddTodo.tsx          # Add new todo form
│   ├── FilterTabs.tsx       # Filter tabs component
│   ├── TodoItem.tsx         # Individual todo item
│   └── TodoList.tsx         # Todo list container
├── services/
│   └── api.ts               # API service layer
└── types/
    └── todo.ts              # TypeScript interfaces
```

## 🎨 Styling

The app uses Tailwind CSS for styling with:
- Custom color palette
- Smooth animations and transitions
- Responsive design patterns
- Custom component classes

## 🔄 Development Mode

When the FastAPI backend is not available, the app will:
- Show sample todo data
- Log API errors to console
- Continue to function for UI development

## 🚀 Production Build

```bash
npm run build
npm start
```

## 📝 Todo Features

- ✅ Add new todos with title and optional description
- ✅ Mark todos as complete/incomplete
- ✅ Edit todo title and description inline
- ✅ Delete todos with confirmation
- ✅ Filter by All, Active, or Completed
- ✅ Responsive design for all screen sizes
- ✅ Smooth animations and transitions
- ✅ Loading states and error handling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
