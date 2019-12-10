moment.locale('es-do');

var app = new Vue({
    delimiters: ['${', '}'],

    el: '#app',
    data: {
        info: {},
        news: [],
        documents: [],
        areas: [],
        mandates: [],
        categories: [],
        searchParams: {
            document_detail: '',
            area: '',
            category: '',
            text: ''
        },
        loading: {
            show: function () {
                $('.spinner').removeClass('d-none');
            },
            hide: function () {
                $('.spinner').addClass('d-none');
            }
        },
    },
    filters: {
        moment: function (date) {
            return moment(date).format('MMMM Do YYYY');
        }
    },
    methods: {
        setFields: function () {
            var document_id = this.searchParams.document_detail;
            var areasPromise = getAreas(document_id);
            var categoryPromise = getCategories(document_id);

            Promise.all([areasPromise, categoryPromise])
                .then((response) => {
                    this.areas = response[0].data;
                    this.categories = response[1].data;
                })
        },
        getMandates: function (e) {
            e.preventDefault();
            getMandates(this.searchParams).then((response) => { this.mandates = response.data })
        }
    },
    created(){
        this.loading.show()
    },
    mounted() {
        var info = getInfo();
        var documents = getDocuments();
        var news = getNews();

        Promise.all([info, documents, news])
            .then((response) => {
                this.info = response[0].data
                this.documents = response[1].data
                this.news = response[2].data
            })
            .finally(() => {
                this.loading.hide()
            })
    }
})

/*
function populate_filter(filter_name, display_name) {

	display_name = display_name || 'name';

	$.get('/api/' + filter_name).then(function (res, header) {
		res.forEach(function (item, i) {

			var selected = '';

			if (values[filter_name] == item.id) selected = 'selected';

			$('#' + filter_name).append('<option ' + selected + ' value="' + item.id + '">' + item[display_name] + '</option>')
		});
	});
}

function filterByArea() {
	$('.area_filter').click(function () {
		var area_id = $(this).data('area');
		$('form #area').val(area_id);
		$('form').submit()
	})
}

function enable_select2() {
	$('.power-select').select2();
}

function onReady() {
	populate_filter('area')
	populate_filter('category')
	populate_filter('source')
	populate_filter('document', 'title')

	enable_select2();
}

function paginate() {

	$('.page-link').click(function (ev) {
		var page = $(this).data('page');
		$('#page').val(page)
		$('form').submit()
	})
}

function resetForm() {
	$('form button[type="reset"]').click(function (ev) {
		window.location = '/'
	})
}

function enableTooltip() {
	$('.badge.badge-secondary').tooltip()
}

$(document).ready(onReady);
$(document).ready(paginate);
$(document).ready(filterByArea);
$(document).ready(enableTooltip);
$(document).ready(resetForm);

*/