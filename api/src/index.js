const express = require('express');
const cors = require('cors');

const productsRouter = require('./routes/products');
const stockRouter = require('./routes/stock');
const ordersRouter = require('./routes/orders');

const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

app.use('/products', productsRouter);
app.use('/stock', stockRouter);
app.use('/orders', ordersRouter);

app.get('/health', (_, res) => res.json({ status: 'ok' }));

app.listen(PORT, () => console.log(`Business API on http://localhost:${PORT}`));