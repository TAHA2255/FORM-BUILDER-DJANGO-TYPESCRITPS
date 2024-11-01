# Form Builder Application

This project is a **Form Builder Application** built with the [formbuilder.dev](https://formbuilder.dev) React library for the frontend and Django as the backend. It enables users to create customizable form widgets with a user-friendly, drag-and-drop interface and dynamically generates embed codes for each form.

## Features
- **Drag-and-Drop Form Building**: Easily add and arrange form elements with a drag-and-drop interface.
- **Customizable Form Widgets**: Create and configure various form widgets, including text fields, checkboxes, radio buttons, dropdowns, and more.
- **Dynamic Configuration Options**: Adjust settings like validation, labels, placeholders, and other attributes for each widget.
- **Embed Code Generation**: Each form widget has a unique embed code generated by the Django backend, making it easy to integrate forms into other websites.
- **Preview Mode**: Instantly preview how your form will appear to end users.

This application provides a convenient way to design and embed forms for different purposes, such as surveys, feedback forms, registrations, and more, without needing to write complex code.


https://github.com/user-attachments/assets/b858fd30-48e8-41b6-99a8-a8ce83c659a1

![328525015-f04cb925-671f-4ae3-9376-3b155e95256a](https://github.com/user-attachments/assets/2c7c9ffe-1620-46a9-90da-30043e1bfb01)

# Backend

<h2>Setup Instructions</h2>
<ol>
    <li><strong>Open PostgreSQL pgAdmin</strong></li>
    <li><strong>Create a Database</strong></li>
    <li><strong>Create <code>.env</code> file in the backend directory</strong></li>
    <li><strong>Copy <code>.env.example</code> file and paste it in <code>.env</code> file</strong></li>
    <li><strong>Fill database fields with the created database configurations</strong></li>
    <li><strong>Update the remaining fields as follows:</strong>
        <ul>
            <li><code>DEBUG=1</code></li>
            <li><code>ALLOWED_HOSTS=127.0.0.1,localhost</code></li>
            <li><code>CORS_ALLOWED_ORIGINS=http://localhost:8080/,http://127.0.0.1:5500/</code></li>
            <li><code>FRONTEND_URL=http://localhost:8000/</code></li>
        </ul>
    </li>
    <li><strong>Run the following commands:</strong>
        <pre>
<code>python manage.py makemigrations
python manage.py migrate
python manage.py runserver</code>
        </pre>
    </li>
</ol>

# Frontend

FormBuilder - is a lightweight, user-friendly, effective and essential form tool used to create and manage forms. It is based on React and
can be integrated into any web app.

For deployment and further development, you will need the following toolkit:

- npm;
- webpack 3 (!);

1. Run the commands in the project's root folder:
   ```bash
   cd demo
   npm install --legacy-peer-deps
   npm run start
   ```

2. Open the sample in a browser (by default at http://localhost:8080/)