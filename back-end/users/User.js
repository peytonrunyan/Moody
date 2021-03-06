const mongoose = require("mongoose");
const ObjectId = mongoose.Schema.Types.ObjectId;

const GENDERS = ["M", "F"];

const User = new mongoose.Schema({
  name: { type: String },
  gender: { type: String, enum: GENDERS },
  age: { type: Number },
  twitter: { type: String },
  days: [{ type: ObjectId, ref: "Day" }],
});

module.exports = mongoose.model("User", User);
