#README.md

- Environment Setting
. git --version
. git config --global user.name 'Aaron Hon-Yu Ma'
. git config --global user.email 'hyma128@pu.edu.tw'
. git init
# browse to check a folder existed called .git

- Test File Building
. create a new file. #README.md and write something.
. save (ctrl + S)
. git add .
. git commit -m 'init readme.md'
. git status #check untracked file or folder
. git log --oneline

- push local Git to cloud GitHub
. browse GitHub
. login GitHub
. Create new repository
. copy the instruction*3 and paste to VS code terminal
. execute

- DB initialization
. create a new file 'product_info.db'
. create new table
. table name = product_info
. add new column: id, name, version, remark

#SELECT
SELECT id, name FROM product_info
WHERE id='2';

#INSERT
INSERT INTO "main"."product_info"
("name", "version", "remark")
VALUES ('Laptop', 'ASUS', 'I love ASUS');

#UPDATE
UPDATE product_info
SET name = 'iPhone', version='18.3'
WHERE id=1;

#DELETE
DELETE FROM product_info
WHERE id=3;