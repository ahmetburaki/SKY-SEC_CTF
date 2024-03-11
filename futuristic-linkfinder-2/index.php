<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Futuristic Link Finder</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <!-- Custom CSS -->
    <style>
        body {
            background-color: #f8f9fa;
        }
        .container {
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <?php 
    if (isset($_GET['debug']) ) {
                //echo("highlight file ");
            highlight_file(__FILE__);
            exit();
            }
    ?>
<div class="container">
    <div class="row">
        <div class="col-md-8 offset-md-2">
        <div class="card">
        <div class="card-header bg-primary text-white">
            <h3 class="card-title">Futuristic Link Finder</h3>
        </div>
        <div class="card-body">
            <form method="GET" action="index.php">
            <div class="form-group">
                <label for="targetURL">Target URL:</label>
                <input type="url" class="form-control" id="targetURL" name="url" placeholder="Enter target URL">
            </div>
            </form>
        </div>
        </div>
    </div>
    </div>
    <div class="row mt-4">
        <div class="col-md-8 offset-md-2">
        <div class="card">
            <div class="card-header bg-success text-white">
            <h5 class="card-title">Discovered Links</h5>
        </div>
        <?php
        if (isset($_GET['url'])) {
            $cmd = "python3 /opt/linkfinder.py ". escapeshellcmd($_GET['url']);
            $file_name = trim(shell_exec($cmd));
            $file = fopen($file_name, "r");
            if ($file) {
                while (!feof($file)) {
                    $line = fgets($file);
                    echo $line . "<br>";
                }
                fclose($file);
            } else {
                echo "Error: Unable to open the file.";
            }

        } 
        ?>
        <div class="card-body">
            <ul class="list-group" id="discoveredLinks">
            <!-- Discovered links will be displayed here -->
            </ul>
        </div>
        </div>
        </div>
    </div>
</div>

    <!-- Bootstrap JS (optional) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
