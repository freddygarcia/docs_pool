var DOCS_API = '/docs/api';
var NEWS_API = '/news/api';

function getDocuments() {
    return axios.get(DOCS_API + '/document/')
}

function getAreas(document_id) {
    return axios.get(DOCS_API + '/area/' + document_id)
}

function getCategories(document_id) {
    return axios.get(DOCS_API + '/category/' + document_id)
}

function getInfo(){
    return axios.get(DOCS_API + '/info')
}

function getMandates(params){
    return axios.get(DOCS_API + '/mandate?' + $.param(params))
}

function getNews(){
    return axios.get(NEWS_API + '/post')
}
