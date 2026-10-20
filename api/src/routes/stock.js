const { Router } = require('express');
const { products, stock } = require('../data/store');
const router = Router();

// GET /stock — all stock levels
router.get('/', (req, res) => {
  const result = Object.entries(stock).map(([productId, quantity]) => ({
    productId,
    name: products[productId]?.name ?? 'Unknown',
    quantity,
    status: quantity === 0 ? 'out_of_stock' : quantity < 10 ? 'low' : 'in_stock',
  }));
  res.json(result);
});

// GET /stock/:id — inventory level
router.get('/:id', (req, res) => {
 const qty = stock[req.params.id];
 if (qty === undefined) return res.status(404).json({ error: 'Product not found' });
 res.json({
 productId: req.params.id,
 quantity: qty,
 status: qty === 0 ? 'out_of_stock' : qty < 10 ? 'low' : 'in_stock',
 });
});

// PUT /stock/:id — inventory update
router.put('/:id', (req, res) => {
 if (!(req.params.id in stock)) return res.status(404).json({ error: 'Product not found' });
 const quantity = Number(req.body.quantity);
 if (isNaN(quantity) || quantity < 0)
  return res.status(400).json({ error: 'quantity must be a non-negative number' });
 stock[req.params.id] = Number(req.body.quantity);
 res.json({ productId: req.params.id, quantity: stock[req.params.id] });
});

module.exports = router;