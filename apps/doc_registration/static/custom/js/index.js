
	function populate_filter(filter_name, display_name) {

		var values = {{ f_filters | safe }};
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