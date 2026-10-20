const products = {
 P001: { id: 'P001', name: 'Laptop Pro X1', price: 1299.99, category: 'IT' },
 P002: { id: 'P002', name: 'Ergonomic Mouse', price: 49.99, category: 'Peripherals' },
 P003: { id: 'P003', name: '27-inch screen', price: 399.99, category: 'Display' },
 P042: { id: 'P042', name: 'Mechanical RGB Keyboard',price: 129.99, category: 'Peripherals' },
};

const stock = { P001: 12, P002: 87, P003: 0, P042: 34 };

const orders = [
 { id: 'CMD001', productId: 'P001', qty: 2, status: 'delivered', client: 'Dupont SARL' },
 { id: 'CMD002', productId: 'P042', qty: 5, status: 'in progress', client: 'Tech Corp' },
 { id: 'CMD003', productId: 'P003', qty: 1, status: 'on hold', client: 'Dupont SARL' },
];

module.exports = { products, stock, orders };