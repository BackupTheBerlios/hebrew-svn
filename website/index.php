<?

$page=$_GET["content"];

if (!($page))
$page="index.txt";

echo "<html>";

echo "<head>";

echo "<title>HEBREW TOOLS COLLECTION PROJECT</title>";

echo "</head>";

echo "<body>";

include "content/menu.txt";

echo "<hr />";

include "content/".$page.".txt";

echo "</body>";

?>