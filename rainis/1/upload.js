const csv = require("csvtojson/v2");
const sanitize = require("./sanitize");
const MongoClient = require('mongodb').MongoClient;
const url = "mongodb://root:example@localhost:27017/";

MongoClient.connect(url, function (err, db) {
    if (err) throw err;

    var dbo = db.db("bigdata");

    csv()
        .fromFile('./data.csv')
        .then(json => {
            console.log(json)
            
            const jsonSanitized = sanitize(json);


            dbo.collection("students").deleteMany({}).then(() => {
                dbo.collection("students").insertMany(jsonSanitized, (err, res) => {
                    if (err) throw err;

                    console.log("1 document inserted");
                    
                    db.close();
                })
            })


        });
});
