docker run -d --net=app_net -p 5432:5432 --name postgresql \
  -e POSTGRES_USER=hackme \
  -e POSTGRES_PASSWORD=hackmepass \
  -e POSTGRES_DB=file_manager \
  postgres:14

# to connect via psql: psql -U hackme -d file_manager -h localhost