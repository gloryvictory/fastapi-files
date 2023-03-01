--SELECT count(*)
--FROM files
--where files.file_path  like '%Снежная%'

--explain SELECT *
--FROM files
--where files.file_path  like '%Снежная%'


-- files.file_path  like '%Снежная%'

-- SELECT f.file_path
-- FROM files f
-- where
-- to_tsvector(f.file_path) @@ to_tsquery('Снежная')

-- ----------------------------------------------------------------------------------------------------
--ALTER TABLE files
--	ADD COLUMN file_path_fts tsvector;
--
--update files
--	set file_path_fts = to_tsvector(coalesce(file_path,''));
--
--
--CREATE INDEX IF NOT EXISTS file_path_fts_idx
--	ON files
--	USING GIN (file_path_fts);


--SELECT f.file_path
--FROM files f
--where file_path_fts @@ to_tsquery('Снежная')
--order by ts_rank(file_path_fts, plainto_tsquery('Снежная'))


SELECT f.file_path
FROM files f
where file_path_fts @@ to_tsquery('подсчет&запасов')
order by ts_rank(file_path_fts, plainto_tsquery('подсчет&запасов'))
