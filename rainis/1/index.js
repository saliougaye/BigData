const MongoClient = require('mongodb').MongoClient;
const url = "mongodb://root:example@localhost:27017/";
const dbname = "bigdata";
const collection = "students";

MongoClient.connect(url, function (err, db) {
    if (err) throw err;

    const dbo = db.db(dbname);

    const countBySex = async () => {

        try {
            const data = await dbo.collection(collection).aggregate([
                {
                    "$group": {
                        _id: "$sesso",
                        count: {
                            "$sum": 1
                        }
                    }
                }
            ]).toArray();

            console.log(data);

        } catch (error) {

            console.log(`Error ${error}`);
        }

        db.close();

    }

    const countByZodiac = async () => {

        try {

            const data = await dbo.collection(collection).aggregate([
                {
                    "$group": {
                        _id: "$segnozodiacale",
                        count: {
                            "$sum": 1
                        }
                    }
                }
            ]).toArray();

            console.log(data);

        } catch (error) {
            console.log(`Error ${error}`);
        }

        db.close();
    }


    const countBySocial = async () => {

        const socials = [
            'facebook',
            'twitter',
            'instagram',
            'linkedin',
            'strava'
        ]

        try {

            const data = await dbo.collection("students").find({}).toArray();

            const students = data.map(s => {

                const student = {
                    id: s.id,
                    name: s.nome,
                    socials: 0
                }

                socials.forEach(el => {
                    if (s[el].toLowerCase() == "si" || s[el].toLowerCase() == "sì") {
                        student.socials += 1;
                    }
                });

                return student;
            });


            console.log(students);
        } catch (error) {
            console.log(`Error ${error}`);
        }

        db.close();
    }


    countBySex()
        .then(() => console.log("completed"));

    
});