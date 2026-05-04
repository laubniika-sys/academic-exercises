let balance = localStorage.getItem("balance");

if (balance === null) {
    balance = 1000;
    localStorage.setItem("balance", balance);
}

balance = Number(balance);

const rates = {
    euro: 1.17,
    real: 5.01,
    yen: 0.0063,
    pound: 1.34
};

function updateBalance(value) {
    balance += value;
    localStorage.setItem("balance", balance);
}

function formatMoney(value) {
    return value.toLocaleString("en-US", {
        style: "currency",
        currency: "USD"
    });
}