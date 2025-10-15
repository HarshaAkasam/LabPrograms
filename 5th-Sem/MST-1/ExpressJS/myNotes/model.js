// 7.c Example mongoose schema (no actual DB connection in demo)
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const NoteSchema = new Schema({
  name: { type: String, required: true },
  content: String
});
module.exports = mongoose.model('Note', NoteSchema);
