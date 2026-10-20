const { Router } = require('express');
const { orders } = require('../data/store');
const router = Router();

// GET /orders — with optional filters ?client=&status=
router.get('/', (req, res) => {
 let result = orders;
 if (req.query.client)
 result = result.filter(o => o.client.toLowerCase().includes(req.query.client.toLowerCase()));
 if (req.query.status)
 result = result.filter(o => o.status === req.query.status);
 res.json(result);
});

// GET /orders/:id — order details
router.get('/:id', (req, res) => {
 const order = orders.find(o => o.id === req.params.id);
 if (!order) return res.status(404).json({ error: 'Order not found' });
 res.json(order);
});

module.exports = router;