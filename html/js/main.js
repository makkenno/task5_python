const addBtn = document.getElementById("add-btn");
const billBtn = document.getElementById("bill-btn");
const payBtn = document.getElementById("pay-btn");
const amountToPayField = document.getElementById('pay_off');

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
      billBtn.disabled = false;
    })
  } else {
    alert("商品コードと注文する個数を適切に入力してください");
    return false;
  }
  document.getElementById("quantity").value = "";
})

billBtn.addEventListener('click', () => {
  const calTotalPrice = async () => {
    return await eel.calculate_total_price()();
  }

  calTotalPrice().then(totalPrice => {
    const totalPriceInputField = document.getElementById('total_price');
    totalPriceInputField.value = totalPrice + "円";
    addBtn.disabled = true;
    amountToPayField.disabled = false;
    billBtn.disabled = true;
    payBtn.disabled = false;

    const productCodeField = document.getElementById('product-code');
    const quantityField = document.getElementById('quantity');
    productCodeField.disabled = true;
    quantityField.disabled = true;
  })
})

payBtn.addEventListener('click', () => {
  const amountToPay = amountToPayField.value;
  const settleBill = async (amountToPay) => {
    return await eel.settle_bill(amountToPay)();
  }

  settleBill(amountToPay)
    .then(change => {
        const changeInputField = document.getElementById('change');
        changeInputField.value = change + '円';
        if(change >= 0) {
          confirm('ご利用ありがとうございました。');
        } else {
          alert('金額が足りません');
          amountToPayField.value = '';
          return false;
        }
    })
    .catch((error) => {
      alert('数字で金額を入力してください');
      amountToPayField.value = '';
      return false;
    })
})
