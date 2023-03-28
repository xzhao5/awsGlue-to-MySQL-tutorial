#import moduals
import sys, getopt

# function to print Author
def print_author():
    from datetime import datetime
    print("")
    print("*"*55)
    print("*"*10+"   Author: Tom Zhao   "+"*"*10)
    print("*"*10+"  "+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"  "+"*"*10)
    print("*"*55)
    print("")



# function to load csv into table
def load_to_table(file,table):
    print('-> Loading...')
    cs.execute('''LOAD DATA LOCAL INFILE '{file}' INTO TABLE {table} FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;'''.format(file=file,table=table))
    print('-> Complete csv file insert successfully...')


# function to insert .csv file
def insert_csv_into_mysql(user, password, table, file, truncate,hosts,db):
    # import errors from mysql connector
    import mysql.connector 
    from mysql.connector import errorcode

    # connect to mysql database
    conn= mysql.connector.connect (
                           user=user,
                           password=password,
                           host=hosts,
                           database=db,
                           allow_local_infile=True
                           )
    
    # open the connection to mysql
    global cs
    cs = conn.cursor(buffered=True)
    # print out connect successfully
    print('Connect to MySQL...')
    # print out truncate option
    print('Your truncate option is "{truncate}"'.format(truncate=truncate))

    try:
        # check if select any database
        cs.execute("select database();")
        print ("-> Pickup database")
        # select our database
        cs.execute("use {db};".format(db=db))
        print ("-> Select database {db}".format(db=db))
        # print out currently running
        print("...")
        # option to truncate the table
        if truncate == "Y":
            print("Now truncating table {table}".format(table=table))
            cs.execute("truncate {table}".format(table=table))
            print("Table truncated")
            print("...")
        else:
            print("Running SQL statemnet...")

        # load csv file into table
        load_to_table(file,table)

        # save the change 
        conn.commit()
        print("Save Change...")

    # print out error if error occurred.
    except mysql.connector.Error as err:
        print(err)
    finally:
        cs.close()
        print("Session Close...")
    cs.close()


# main function to start my application: 
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"ou:p:t:f:d:h:e:")
    except getopt.GetoptError as err:
        print(err)
        print('main.py -u <user> -p <password> -t <table_name> -f <file_path> -d <truncate_option> -h <host_name> -e <databse_name>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-o':
            print('main.py -u <user> -p <password> -t <table_name> -f <file_path> -d <truncate_option> -h <host_name> -e <databse_name>')
            sys.exit()
        elif opt in ("-u"):
            user = arg
        elif opt in ("-p"):
            password = arg
        elif opt in ("-t"):
            table = arg
        elif opt in ("-f"):
            file = arg    
        elif opt in ("-d"):
            truncate = arg 
        elif opt in ("-h"):
            hosts = arg 
        elif opt in ("-e"):
            db = arg
    insert_csv_into_mysql(user, password, table, file, truncate,hosts,db)
    print_author()

if __name__ == "__main__":
    main()
