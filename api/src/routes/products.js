const { Router } = require('express');
const { products } = require('../data/store');
const router = Router();

// GET /products — list all products
router.get('/', (req, res) => {
 const { category } = req.query;
 let result = Object.values(products);
 if (category) result = result.filter(p => p.category === category);
 res.json(result);
});

// GET /products/:id — product detail
router.get('/:id', (req, res) => {
 const product = products[req.params.id];
 if (!product) return res.status(404).json({ error: 'Product not found' });
 res.json(product);
});

module.exports = router;