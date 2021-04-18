window.onload=function() {
  let dataImage = localStorage.getItem('invoice_logo');
  document.getElementById('logo').src = dataImage;

  let price_total = Array.from(document.getElementsByClassName('subtotal')).reduce(
    (acc, el) => acc + parseFloat(el.innerText), 0
  );
  document.getElementById("total").innerHTML = isNaN(price_total) ? "0.00": price_total.toFixed(2);
}