<?php

set_time_limit(0);
ini_set('memory_limit', '10240M');
include_once "app/Mage.php";
//include_once "downloader/Maged/Controller.php";

Mage::init();

$app = Mage::app('default');

/* $attributeSetCollection = Mage::getResourceModel('eav/entity_attribute_set_collection') ->load();

foreach ($attributeSetCollection as $id=>$attributeSet) {
  $entityTypeId = $attributeSet->getEntityTypeId();
  $name = $attributeSet->getAttributeSetName();
 echo "ATTRIBUTE SET :".$name." - ".$id;
} */

function fromcsv(){
if (($handle = fopen("rapnet.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        echo 'Importing product: '.$data[0].'<br />';
       
        $num = count($data);
        //echo "<p> $num fields in line $row: <br /></p>\n";
        $row++;
 	$fullpath='var/import/solitairenew.jpg';   
       
        
        //echo "SKU: " . $row["SKU"]. " - Weight: " . $row["Weight"]. " " . $row["Color"]. "<br>";
		$product = Mage::getModel('catalog/product');
		$product->setSku($data[13]);
		$name='solitare'+$data[13];
		$product->setName($name);
		$product->setDescription('my first solitaire');
		$product->setShortDescription('my first solitaire');
		$product->setManufacturer('');
		$product->setPrice($data[10]);
		$product->setTypeId('simple');
		$product->addImageToMediaGallery($fullpath, 'thumbnail', false);
		$product->addImageToMediaGallery($fullpath, 'small-image', false);
		$product->addImageToMediaGallery($fullpath, 'image', false);
		$product->setAttributeSetId(10); // need to look this up
		$categories = array(31);

		$product->setCategoryIds($categories); // need to look these up
		$product->setWeight($data[1]);
		$product->setColor2($data[2]);
		$product->setClarity($data[3]);
		$product->setShape($data[0]);		
		$product->setPolish($data[5]);
		$product->setCut($data[4]);		
		$product->setSolitSymmetry($data[6]);
		$product->setFluorescence($data[7]);
		$product->setCertificate($data[8]);
		$product->setDiscount($data[9]);
		$product->setTotal($data[10]);
		$product->setRapaport($data[11]);		
		$product->setTaxClassId(0); // taxable goods
		$product->setVisibility(4); // catalog, search
		$product->setStatus(1); // enabled

		// assign product to the default website
		$product->setWebsiteIds(array(Mage::app()->getStore(true)->getWebsite()->getId()));


		$stockData = $product->getStockData();
		$stockData['qty'] = 100; //18
		$stockData['is_in_stock'] =1; //17
		$stockData['manage_stock'] = 1;
		$stockData['use_config_manage_stock'] = 0;
		$product->setStockData($stockData);


		$product->save();    
       
        
    }
    fclose($handle);
    
}
}
fromcsv();
function fromdatabase() {
$con1=mysqli_connect('localhost', 'user', 'password','database') or die('cannot connect');
$sql = "select * from solitaire_amrin limit 200";
$result = $con1->query($sql);

echo 'starting product upload';	
if ($result->num_rows > 0) {
    // output data of each row
	$fullpath='var/import/solitairenew.jpg';
    while($row = $result->fetch_assoc()) {
        //echo "SKU: " . $row["SKU"]. " - Weight: " . $row["Weight"]. " " . $row["Color"]. "<br>";
		$product = Mage::getModel('catalog/product');
		$product->setSku($row["SKU"]);
		$name='solitare'+$row["SKU"];
		$product->setName($name);
		$product->setDescription('my first solitaire');
		$product->setShortDescription('my first solitaire');
		$product->setManufacturer('');
		$product->setPrice($row['Total Price']);
		$product->setTypeId('simple');
		$product->addImageToMediaGallery($fullpath, 'thumbnail', false);
		$product->addImageToMediaGallery($fullpath, 'small-image', false);
		$product->addImageToMediaGallery($fullpath, 'image', false);
		$product->setAttributeSetId(10); // need to look this up
		$categories = array(31);

		$product->setCategoryIds($categories); // need to look these up
		$product->setWeight($row["Weight"]);
		$product->setColor2($row["Color"]);
		$product->setClarity($row["Clarity"]);
		$product->setShape($row["Shape"]);		
		$product->setPolish($row["Polish"]);
		$product->setCut($row["Cut"]);		
		$product->setSymmetry($row["Symmetry"]);
		$product->setFluorescence($row["Fluorescence"]);
		$product->setCertificate($row["Certificate Number"]);
		$product->setDiscount($row["Discount"]);
		$product->setTotal($row["Total Price"]);
		$product->setRapaport($row["Rapaport Price in Rs"]);		
		$product->setTaxClassId(0); // taxable goods
		$product->setVisibility(4); // catalog, search
		$product->setStatus(1); // enabled

		// assign product to the default website
		$product->setWebsiteIds(array(Mage::app()->getStore(true)->getWebsite()->getId()));


		$stockData = $product->getStockData();
		$stockData['qty'] = 100; //18
		$stockData['is_in_stock'] =1; //17
		$stockData['manage_stock'] = 1;
		$stockData['use_config_manage_stock'] = 0;
		$product->setStockData($stockData);


		$product->save(); 
		#print_r(array_keys($product));
		echo 'one down <br>';
    }
} else {
    echo "0 results";
}	
}
//fromdatabase() ;
   

?>