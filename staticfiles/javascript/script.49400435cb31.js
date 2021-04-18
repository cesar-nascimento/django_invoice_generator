function calc(index) {
  let price = parseFloat(document.getElementById("id_form-"+index+"-quantity").value)*
              parseFloat(document.getElementById("id_form-"+index+"-unit_price").value);
  document.getElementById("subtotal-" + index).firstChild.nodeValue = isNaN(price) ? "0.00": price.toFixed(2);

  let price_total = Array.from(document.getElementsByClassName('subtotal')).reduce(
    (acc, el) => acc + parseFloat(el.innerText), 0
  );

  document.getElementById("total").innerHTML = isNaN(price_total) ? "0.00": price_total.toFixed(2);
}
window.onload=function() {
  document.getElementById("id_form-0-quantity").addEventListener('input', function(){calc(0);});
  document.getElementById("id_form-0-unit_price").addEventListener('input', function(){calc(0);});
  document.getElementById("id_invoice_logo").onchange = function () {
    let reader = new FileReader();

    reader.onload = function (e) {
        // get loaded data and render thumbnail.
        localStorage.setItem("invoice_logo", e.target.result);
        document.getElementById("logo").src = e.target.result;

    };

    // read the image file as a data URL.
    reader.readAsDataURL(this.files[0]);
  };
  $('.item-formset').formset({
    addText: 'add item',
    deleteText: 'remove',
    added: function (row) {
      let index = row[0].rowIndex;

      let thead_element = row[0].querySelector('th');
      thead_element.innerHTML = index;

      let index_zero_start = index - 1;
      let quantity_element = row[0].querySelector('td:nth-of-type(2)');
      quantity_element.addEventListener('input', function(){calc(index_zero_start);});

      let price_element = row[0].querySelector("td:nth-of-type(3)");
      price_element.addEventListener('input', function(){calc(index_zero_start);});

      let subtotal = row[0].querySelector("td:nth-of-type(4)");
      subtotal.setAttribute("id", "subtotal-" + index_zero_start);

    },
});
}