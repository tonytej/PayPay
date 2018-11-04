from json2html import *
input = {
  "Transaction ID": "1234678910",
  "Products": [
    {
      "Product ID": "9I879871",
      "Product Name": "Nasi Goreng",
      "Price": 15000
    },
    {
      "Product ID": "987986",
      "Product Name": "Bakso Kuah",
      "Price": 70000
    },
    {
      "Product ID": "46546542333",
      "Product Name": "Martabak Keju",
      "Price": 54000
    }
  ]
}

Html_file= open("albert.html","w")

Html_file.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Table V02</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->  
  <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
  <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
  <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
  <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
  <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
  <link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
<!--===============================================================================================-->

  <link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>
<body>
  
  <div class="limiter">
    <div class="container-table100">
      <div class="wrap-table100">
          <table border="1"><tr><th>Transaction ID</th><td>1234678910</td></tr><tr><th>Products</th><td><table border="1"><tr><th>Product ID</th><th>Price</th><th>Product Name</th></tr><tr><td>9I879871</td><td>15000</td><td>Nasi Goreng</td></tr><tr><td>987986</td><td>70000</td><td>Bakso Kuah</td></tr><tr><td>46546542333</td><td>54000</td><td>Martabak Keju</td></tr></table></td></tr></table>

          </div>
      </div>
    </div>
  </div>


  

<!--===============================================================================================-->  
  <script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
  <script src="vendor/bootstrap/js/popper.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
  <script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
  <script src="js/main.js"></script>

</body>
</html>""")


print(json2html.convert(json = input))
