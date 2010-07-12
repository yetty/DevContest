<?php
$r = fopen('php://stdin', 'r');

$n = (int) fgets($r, 1024);

for($i=0;$i<$n;$i++) {
	$line = fgets($r, 1024);
	list($a, $b) = explode(" ", $line);
	print (string)((int) $a * (int) $b)."\n";
}
