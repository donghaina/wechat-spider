let dataTables = DataTables.default;

Vue.component('table-detail', {
    template: '#table-detail-template',
    components: {dataTables},
    data: function () {
        return {
            tableData: [],
            dialogFormVisible: false,
            form: {
                id: '',
                wx_id: '',
                wx_title: '',
                scraping_time: '',
            },
            formType: 'create',
            formTitle: '添加公众号'
        }
    },
    mounted: function () {
        this.getFeedList();
    },
    methods: {
        getActionsDef: function () {
            let self = this;
            return {
                width: 5,
                def: [{
                    name: '添加数据',
                    handler() {
                        self.formType = 'create';
                        self.formTitle = '添加数据';
                        self.form.id = '';
                        self.form.wx_id = '';
                        self.form.wx_title = '';
                        self.form.scraping_time = '';
                        self.dialogFormVisible = true;
                    },
                    icon: 'plus'
                }]
            }
        },
        getPaginationDef: function () {
            return {
                pageSize: 10,
                pageSizes: [10, 20, 50]
            }
        },
        getRowActionsDef: function () {
            let self = this;
            return [{
                type: 'primary',
                handler(row) {
                    self.formType = 'edit';
                    self.form.id = row.id;
                    self.form.wx_id = row.wx_id;
                    self.form.wx_title = wx_title;
                    self.form.scraping_time =row.scraping_time;
                    self.formTitle = '编辑数据';
                    self.dialogFormVisible = true;
                },
                name: '编辑'
            }, {
                type: 'danger',
                handler(row) {
                        self.$confirm('确认删除该数据?', '提示', {
                            confirmButtonText: '确定',
                            cancelButtonText: '取消',
                            type: 'warning'
                        }).then(function () {
                            let url = Flask.url_for("delete_feed", {feed_id: row.id});
                            axios.delete(url).then(function (response) {
                                self.getFeedList();
                                self.$message.success("删除成功！")
                            }).catch(self.showError)
                        });
                },
                name: '删除'
            }]
        },
        getFeedList: function () {
            let url = Flask.url_for("get_feed_list");
            let self = this;
            axios.get(url).then(function (response) {
                self.tableData = response.data.feed_list;
            });
        },
        createOrUpdate: function () {
            let self = this;
            if (self.form.wx_id === '' || self.form.wx_title==='') {
                self.$message.error('公众号信息不能为空！');
                return
            }
            console.log(self.formType);
            if (self.formType === 'create') {
                let url = Flask.url_for("add_feed");
                axios.post(url, {
                    wx_id: self.form.wx_id,
                    wx_title: self.form.wx_title,
                    scraping_time: self.form.scraping_time,
                }).then(function (response) {
                    self.getFeedList();
                    self.dialogFormVisible = false;
                    self.$message.success('添加成功！')
                }).catch(self.showError);
            } else {
                let url = Flask.url_for("update_feed", {feed_id: row.id});
                axios.put(url, {
                    wx_id: self.form.wx_id,
                    wx_title: self.form.wx_title,
                    scraping_time: self.form.scraping_time,
                }).then(function (response) {
                    self.getFeedList();
                    self.dialogFormVisible = false;
                    self.$message.success('修改成功！')
                }).catch(self.showError);
            }
        },
        showError: function (error) {
            let response = error.response;
            this.$message.error(response.data.message);
        }
    }
});

new Vue({
    el: '#wechat_spider'
});