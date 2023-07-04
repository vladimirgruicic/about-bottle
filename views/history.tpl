<!-- views/history.tpl -->
<!DOCTYPE html>
<html>
<head>
  <title>History</title>
  <link rel="stylesheet" type="text/css" href="/static/css/history.css">
  <script src="/static/js/history.js"></script>
</head>
<body>
  <include file="nav.tpl" />

  <h1>This is club history page!</h1>
  <!-- Other content goes here -->

  <div class="dropdown">
        <button class="dropbtn" onmouseover="showDropdown()">Dropdown</button>
        <div class="dropdown-content" onmouseleave="hideDropdown()">
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
            <a href="/zlatan">Zlatan</a>
        </div>
    </div>     
</body>
</html>