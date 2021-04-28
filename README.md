# colector


# Pure postgresSQL API
a set of PostgreSQL functions written in PLPGSQL:
```sql
drop schema if exists dox cascade;
create schema dox;
```


The save function will create the customers table if it doesn’t exist and save the JSON.
```sql
select * from dox.save(table => 'customers', doc => '[wad of json]');
```

Auto-explicativas
```sql
select * from dox.find_one(collection => 'customers', term => '{"name": "Jill"}');
select * from dox.find(collection => 'customers', term => '{"company": "Red:4"}');
```


One thing that other systems don’t have which PostgreSQL has built in is full-text indexing. This means you can do fuzzy searches on simple terms with an index rather than a full table scan, which will make your DBA quite happy.


There’s nothing you need to do to enable this, aside from following a simple convention. Every document table comes with a tsvector search field:
```sql
create table customers(
  id serial primary key not null,
  body jsonb not null,
  search tsvector, --this one here
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

When you save a document with a “descriptive key”, it will automatically get dropped into the tsvector search field and indexed:
```sql
search text[] = array['name','email','first','first_name','last','last_name','description','title','city','state','address','street', 'company']
```