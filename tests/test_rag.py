import unittest
from rag_core import load_documents,chunk_documents,Retriever,retrieve,offline_answer
class RagTests(unittest.TestCase):
 def test_docs_valid(self): self.assertEqual(len(load_documents()),8)
 def test_chunks_have_source(self):
  chunks=chunk_documents(load_documents(),size=15,overlap=3)
  self.assertTrue(len(chunks)>8)
  self.assertTrue(all('#c' in c['id'] and c['documento_id'] for c in chunks))
 def test_recovery(self): self.assertIn('DOC-02',{c['documento_id'] for c in retrieve('envíos Lima días hábiles')})
 def test_abstention(self): self.assertEqual(retrieve('astronauta cuásar xylophone'),[])
 def test_no_fake_generation(self): self.assertIn('extractos',offline_answer('envíos',retrieve('envíos')))
 def test_bad_overlap(self):
  with self.assertRaises(ValueError):chunk_documents(load_documents(),5,5)
if __name__=='__main__':unittest.main()
