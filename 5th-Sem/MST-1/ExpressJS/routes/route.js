// 7.a Example express route definitions
const express = require('express');
const router = express.Router();

router.get('/notes/:id', (req,res)=>{
  res.json({ id: req.params.id, note: 'Sample note for id ' + req.params.id });
});

router.put('/notes/:name', (req,res)=>{
  // In real app, update document by name
  res.json({ updated: req.params.name, body: req.body });
});

router.delete('/notes/:name', (req,res)=>{
  // In real app, delete document by name
  res.json({ deleted: req.params.name });
});

module.exports = router;
