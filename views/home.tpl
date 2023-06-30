<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/static/css/home.css"
</head>
<body>
    <div class="container">
        <h1>Welcome to the Home Page</h1>

        <form method="post" action="/">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <input type="submit" value="Submit">
        </form>

        <!-- Add the success message display logic -->
        % if success_message:
            <p>{{ success_message }}</p>
        % end
    </div>
</body>
</html>
