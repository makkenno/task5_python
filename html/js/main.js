const addBtn = document.getElementById("add-btn");
addBtn.addEventListener('click', () => {
  const productCode = document.getElementById("product-code").value;
  const quantity = document.getElementById("quantity").value;

  // 自然数かどうかを判定
  const isNatureNum = (num) => {
    try {
      const numInt = parseInt(num);
      return numInt > 0 && Number.isInteger(numInt);
    } catch(e) {
      alert("個数を入力してください");
      return false;
    }
  }

  const addOrder = async () => {
    const orderSubtotalArray = await eel.add_order(productCode,quantity)();
    return orderSubtotalArray;
  }

  if(productCode !== "商品コード" && isNatureNum(quantity)) {
    addOrder(productCode,quantity).then(orderSubtotalArray => {
      const table = document.getElementById('Table');
      const newRow = table.insertRow();
      
      orderSubtotalArray.forEach(cellText => {
        const newCell = newRow.insertCell();
        const newText = document.createTextNode(cellText);
        newCell.appendChild(newText);
      });
    })
  } else {
    alert("商品コードと注文する個数を適切に入力してください");
    return false;
  }

  document.getElementById("quantity").value = "";
})


const billBtn = document.getElementById("bill-btn");
const payBtn = document.getElementById("pay-btn");
