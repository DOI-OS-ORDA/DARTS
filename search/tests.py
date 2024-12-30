from django.test import TestCase

# Create your tests here.
'''
describe Operations::DocumentSearch do

  let(:documents_folder) { "tests/fixtures/documents/*" }
  let(:import) { DocumentImport.call(documents_folder) }

  before { import }

  let(:search_term) { "bat" }
  subject { Operations::DocumentSearch.new(search_term) }

  context "with matching documents" do
    it "returns matching results" do
      expect(subject.call).to have_entry_matching("A study of vampire bats")
    end

    it "does not return incorrect results" do
      expect(subject.call).to_not have_entry_matching("Leon Battista Alberti")
    end

    it "ranks matches appropriately" do
      expect(subject.call).
        to.
        rank_result("A study of vampire bats").
        above_result("A document that rarely mentions the bats")
    end
  end

  context "with no documents" do
    before { DocumentsRepository.clear }
    it "returns no results" do
      expect(subject.call).to be_empty
    end
  end

end

'''
