var template = `
<select style="width: 900px;">
<slot></slot>
</select>
`

Vue.component('select2', {
    props: ['options', 'value'],
    template: template,
    mounted: function () {
        var vm = this
        $(this.$el)
            // init select2
            .select2({ data: this.options })
            .trigger('change')
            // emit event on change.
            .on('change', function () {
                vm.$emit('input', this.value)
            })
    },
    watch: {
        options: function (options) {
            // value field
            var v_field = this.$attrs['data-v_field'] || 'id';
            // display field
            var d_field = this.$attrs['data-d_field'] || 'title';

            options.map((e) => {
                e.id = e[v_field];
                e.text = e[d_field];
            });

            $(this.$el).empty()
                .select2({ data: options })
                .trigger('change')
        }
    },
    destroyed: function () {
        $(this.$el).off().select2('destroy')
    }
})
