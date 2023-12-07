FROM mongo

COPY init.json /init.json
CMD mongoimport --host mongodb --db dev --collection devCollection --type json --file /init.json --jsonArray
# CMD mongoimport --host mongodb --ssl --username dbuser --password hardpass --db dev --collection devCollection --type json --file /init.json --jsonArray