# Q 0 : # @board.messages.find_by_id(params[:id])
Query(Message)
.where('board_id = ?')
.where('id = ?')
# Q 1 : # @board.messages.includes(:parent).find(params[:id])
Query(Message)
.where('board_id = ?')
.where('id = ?')
# Q 2 : # @board.messages.reorder(:id => :desc).includes(:author, :board).limit(Setting.feeds_limit.to_i).to_a
Query(Message)
.where('board_id = ?')
.order('id')
.includes('author')
.includes('board')
.return_limit('10')
# Q 3 : # @board.topics.reorder(:sticky => :desc).limit(@topic_pages.per_page).offset(@topic_pages.offset).order(sort_clause).preload(:author, { :last_reply => :author }).to_a
Query(Message)
.where('board_id = ?')
.where('parent_id = 0')
.order('sticky')
# Q 4 : # @changeset.filechanges.limit(1000).reorder("path").collect do |change|
#   
#   case change.action
#   when "A"
#     
#     if !change.from_path.blank?
#       
#       changeaction = @changeset.filechanges.detect { |c|
#         
#         c.action == "D" && c.path == change.from_path
#       } ? "R" : "C"
#     end
#     change when "D"
#     
#     @changeset.filechanges.detect { |c|
#       
#       c.from_path == change.path
#     } ? nil : change
#   else
#     
#     change
#   end
#   
# end.compact
Query(Change)
.where('changeset_id = ?')
.order('id, path')
.where('id != 0')
# Q 5 : # @custom_field.enumerations.find(params[:id])
Query(CustomFieldEnumeration)
.where('custom_field_id = ?')
.where('id = ?')
# Q 6 : # @custom_field.enumerations.find_by_id(params[:reassign_to_id])
Query(CustomFieldEnumeration)
.where('custom_field_id = ?')
.where('id = ?')
# Q 7 : # @custom_field.enumerations.order(:position)
Query(CustomFieldEnumeration)
.where('custom_field_id = ?')
.order('position')
# Q 8 : # @enumeration.class.find_by_id(params[:reassign_to_id].to_i)
Query(Enumeration)
.where('id = ?')
# Q 9 : # @group.users
Query(User)
.where('id = ?')
# Q 10 : # @group.users.delete(User.find(params[:user_id]))
Query(User)
.where('id = ?')
# Q 11 : # @issue.changesets.visible.preload(:repository, :user).exists?
Query(Changeset)
.where('id = ?')
.includes('repository')
.includes('user')
.return_limit('1')
# Q 12 : # @issue.changesets.visible.preload(:repository, :user).to_a
Query(Changeset)
.where('id = ?')
.includes('repository')
.includes('user')
# Q 13 : # @issue.changesets.visible.preload(:repository, :user).to_a
Query(Changeset)
.where('id = ?')
.includes('repository')
.includes('user')
# Q 15 : # @issue.time_entries.visible.preload(:activity, :user)
Query(TimeEntry)
.where('issue_id = ?')
.includes('activity')
.includes('user')
# Q 16 : # @issue.time_entries.visible.preload(:activity, :user).to_a
Query(TimeEntry)
.where('issue_id = ?')
.includes('activity')
.includes('user')
# Q 17 : # @issues.collect(&:project).uniq
Query(Issue)
.select('project_id')
.distinct('')
# Q 18 : # @issues.map(&:editable_custom_fields).reduce(:&).reject(&:multiple?).select
# Q 19 : # @journal.details.find_by_id(params[:detail_id])
Query(JournalDetail)
.where('journal_id = ?')
.where('id = ?')
# Q 20 : # @journal.issue.visible_journals_with_index.find { |j|
#   
#   j.id == @journal.id
# }.indice
# Q 21 : # @news.comments.find(params[:comment_id]).destroy
Query(Comment)
.where('news_id = ?')
.where('id = ?')
# Q 22 : # @project.boards.find(params[:id])
Query(Board)
.where('project_id = ?')
.where('id = ?')
# Q 23 : # @project.boards.preload(:last_message => :author).to_a
Query(Board)
.where('project_id = ?')
.includes('last_message => author')
# Q 24 : # @project.documents.includes(:attachments, :category).to_a
Query(Document)
.where('project_id = ?')
.includes('category')
# Q 25 : # @project.issue_categories.find_by_id(params[:reassign_to_id])
Query(IssueCategory)
.where('project_id = ?')
.where('id = ?')
# Q 26 : # @project.issues.find_by_id(params[:reassign_to_id])
Query(Issue)
.where('project_id = ?')
.where('id = ?')
# Q 27 : # @project.news.limit(5).includes(:author, :project).reorder("News.created_on DESC").to_a
Query(News)
.where('project_id = ?')
.return_limit('5')
.includes('author')
.includes('project')
.order('id, created_on')
# Q 28 : # @project.repositories.find_by_identifier_param(params[:repository_id])
# Query(Repository)
# .where('project_id = ?')
# .where('identifier_param = ?')
# Q 29 : # @project.rolled_up_versions.visible.preload(:custom_values)
# Q 30 : # @project.self_and_descendants.pluck(:id)
Query(Project)
.where('(id = ?) || (parent_id = ?)')
.select('id')
# Q 31 : # @project.versions.find_by_id(version_id)
Query(Version)
.where('project_id = ?')
.where('id = ?')
# Q 32 : # @project.versions.includes(:attachments).references(:attachments).reorder(sort_clause).to_a.sort.reverse
Query(Version)
.where('project_id = ?')
# Q 33 : # @query.group_by
# Q 34 : # @query.issue_ids(:limit => (
# limit + 1))
# Q 42 : # @repository.changesets.limit(@changeset_pages.per_page).offset(@changeset_pages.offset).includes(:user, :repository, :parents).to_a
Query(Changeset)
.where('repository_id = ?')
.includes('user')
.includes('repository')
.includes('parents')
# Q 43 : # @time_entries.collect(&:project).compact.uniq
Query(TimeEntry)
.select('project_id')
.where('id != 0')
.distinct('')
# Q 44 : # @time_entries.collect(&:project).compact.uniq
Query(TimeEntry)
.where('id != 0')
.distinct('')
# Q 45 : # @time_entries.map(&:editable_custom_fields).reduce(:&).reject(&:multiple?).select
# Q 46 : # @trackers.map(&:custom_fields).flatten.uniq.sort
# Q 47 : # @user.email_addresses.order(:id).where(:is_default => false).to_a
Query(EmailAddress)
.where('user_id = ?')
.order('id')
.where('is_default = false')
# Q 48 : # @user.email_addresses.where(:is_default => false).find(params[:id])
Query(EmailAddress)
.where('user_id = ?')
.where('is_default = false')
.where('id = ?')
# Q 49 : # @user.memberships.preload(:roles, :project).where(Project.visible_condition(User.current)).to_a
# Q 50 : # @version.fixed_issues.visible.includes(:status, :tracker, :priority).preload(:project).reorder("Tracker.position, Issue.id").to_a
Query(Issue)
.where('fixed_version_id = ?')
.includes('status')
.includes('tracker')
.includes('priority')
.includes('project')
.order('tracker.position, id')
# Q 51 : # @versions.select(&:completed?).reverse
# Query(Version)
# .select('completed')
# Q 52 : # @wiki.pages.find_by_id(params[:reassign_to_id].to_i)
Query(WikiPage)
.where('wiki_id = ?')
.where('id = ?')
# Q 53 : # @wiki.pages.order("title").includes([:content, { :attachments => :author }]).to_a
Query(WikiPage)
.where('wiki_id = ?')
.order('title')
# Q 54 : # @wiki.pages.with_updated_on.reorder("WikiPage.title").includes(:wiki => :project).includes(:parent).to_a
Query(WikiPage)
.where('wiki_id = ?')
.order('title')
.includes('wiki => project')
# Q 55 : # AnonymousUser.unscoped.create(:lastname => "Anonymous", :firstname => "", :login => "", :status => 0)
# Q 56 : # AnonymousUser.unscoped.find_by(:lastname => "Anonymous")
Query(AnonymousUser)
.where('lastname = ?')
# Q 57 : # Array(values_for(field)).select(&:present?)
# Q 58 : # Attachment.find(params[:id])
Query(Attachment)
.where('id = ?')
# Q 59 : # Attachment.find_by(:id => attachment_id, :digest => attachment_digest)
Query(Attachment)
.where('id = ?')
.where('digest = ?')
# Q 60 : # Attachment.find_by(:id => custom_value.value.to_s)
Query(Attachment)
.where('id = ?')
# Q 61 : # Attachment.find_by(:id => custom_value.value.to_s)
Query(Attachment)
.where('id = ?')
# Q 62 : # Attachment.find_by(:id => custom_value.value_before_last_save.to_s)
Query(Attachment)
.where('id = ?')
# Q 63 : # Attachment.find_by_id(custom_value.value)
Query(Attachment)
.where('id = ?')
# Q 64 : # Attachment.find_by_id(id)
Query(Attachment)
.where('id = ?')
# Q 65 : # Attachment.find_by_id(value.to_i)
Query(Attachment)
.where('id = ?')
# Q 69 : # Attachment.where("created_on < ? AND (container_type IS NULL OR container_type = '')", Time.now - age).destroy_all
Query(Attachment)
.where('created_on < ?')
.where("(container_type = NULL) || (container_type = '')")
# Q 70 : # Attachment.where("disk_directory IS NULL OR disk_directory = ''").find_each
Query(Attachment)
.where("(disk_directory = NULL) || (disk_directory = '')")
# Q 71 : # Attachment.where("disk_filename = ? AND id <> ?", disk_filename, id).empty?
Query(Attachment)
.where("disk_filename = ?").where('id <> ?')
# Q 72 : # Attachment.where("length(digest) < 64").find_each
# Q 73 : # Attachment.where(:id => ids).select(&:thumbnailable?)
Query(Attachment)
.where('id = ?')
# Q 74 : # Attachment.where(digest: self.digest, filesize: self.filesize).where("id <> ? and disk_filename <> ?", self.id, self.disk_filename).first
Query(Attachment)
.where('digest = ?')
.where('filesize = ?')
.where('id <> ?')
.where('disk_filename <> ?')
.return_limit('1')
# Q 75 : # AuthSource.find(params[:id])
# Q 77 : # Board.includes(:project).find(params[:board_id])
Query(Board)
.includes('project')
.where('id = ?')
# Q 78 : # Board.visible.find_by_id(oid)
Query(Board)
.where('id = ?')
# Q 79 : # Change.create(:changeset => self, :action => change[:action], :path => change[:path], :from_path => change[:from_path], :from_revision => change[:from_revision])
# Q 80 : # Change.includes(:changeset).where("Change.revision = ? and Changeset.repository_id = ?", e.lastrev.revision, id).order("Changeset.revision DESC").first
Query(Change)
.includes('changeset')
.order('id, revision')
.return_limit('1')
# Q 81 : # Change.joins(:changeset).where("Changeset.repository_id = ? AND Changeset.commit_date BETWEEN ? AND ?", repository.id, date_from, date_to).group(:commit_date).count
Query(Change)
.joins('changeset')
.where("changeset.repository_id = ?")
.where("changeset.commit_date < ?")
.where("changeset.commit_date > ?")
.group('changeset.commit_date')
# Q 82 : # Change.joins(:changeset).where("Changeset.repository_id = ?", id).select("committer, user_id, count(*) as count").group("committer, user_id")
Change
.joins('changeset')
.where("changeset.repository_id = ?")
.select('changeset.committer, changeset.user_id')
.group('changeset.committer, changeset.user_id')
# Q 83 : # Changeset.order("committed_on ASC, id ASC").where("repository_id = ? AND revision LIKE 'tmp%'", id).each
Changeset
.where('repository_id = ?')
.where('revision = ?')
.order('id, committed_on')
# Q 84 : # Changeset.visible.find_by_repository_id_and_revision(repository.id, identifier)
Changeset
.where('repository_id = ?')
.where('revision = ?')
# Q 85 : # Changeset.visible.where("repository_id = ? AND scmid LIKE ?", repository.id, "#{
# name}%").first
Changeset
.return_limit('1')
# Q 86 : # Changeset.where("repository_id = ? AND commit_date BETWEEN ? AND ?", repository.id, date_from, date_to).group(:commit_date).count
Changeset
.where("repository_id = ?")
.where("commit_date < ?")
.where("commit_date > ?")
.group('commit_date')
# Q 87 : # Changeset.where("repository_id = ?", id).select("committer, user_id, count(*) as count").group("committer, user_id")
Changeset
.where('repository_id = ?')
.select('committer, user_id')
.group('committer, user_id')
# Q 88 : # Changeset.where(:repository_id => id).distinct.pluck(:committer, :user_id)
Changeset
.where('repository_id = ?')
.distinct('')
.select('committer')
.select('user_id')
# Q 89 : # Changeset.where(["id < ? AND repository_id = ?", id, repository_id]).order("id DESC").first
Changeset
.where('(id > ?) && (repository_id = ?)')
.order('id')
.return_limit('1')
# Q 90 : # Changeset.where(["id > ? AND repository_id = ?", id, repository_id]).order("id ASC").first
Changeset
.where('(id > ?) && (repository_id = ?)')
.order('id')
.return_limit('1')
# Q 91 : # Changeset.where(["repository_id = ? AND committer = ?", id, committer]).update_all("user_id = #{
# new_user_id.nil? ? "NULL" : new_user_id}")
Changeset
.where('repository_id = ?')
.where('committer = ?')
# Q 92 : # CustomField.find(params[:custom_field_id])
CustomField
.where('id = ?')
# Q 93 : # CustomField.find(params[:id])
CustomField
.where('id = ?')
# Q 94 : # CustomField.find_by_id(prop_key)
CustomField
.where('id = ?')
# Q 95 : # CustomField.visible.where(:is_filter => true).group_by(&:class)
CustomField
.select('visible')
.where('is_filter = true')
# Q 96 : # CustomField.where("type = '#{
# self.class.name}CustomField'").sorted.to_a
CustomField
.where('type = ?')
# Q 97 : # CustomField.where(:id => field_ids).inject({ })
CustomField
.where('id = ?')
# Q 98 : # CustomField.where(:is_filter => true, :type => "#{
# klass.name}CustomField").each
CustomField
.where('is_filter = true')
.where('type = ?')
# Q 99 : # CustomField.where(:type => "#{
# self.name}CustomField", :searchable => true).to_a
CustomField
.where('type = ?')
.where('searchable = true')
# Q 100 : # CustomValue.joins(:custom_field).where(:value => id.to_s, :custom_fields => { :field_format => "version" }).any?
CustomValue
.joins('custom_field')
.where('value = ?')
.where('custom_field.field_format = ?')
# Q 101 : # Document.visible.find_by_id(oid)
Document
.where('id = ?')
# Q 102 : # Document.visible.order("Document.created_on DESC").limit(10).to_a
Document
.order('created_on')
.return_limit('10')
# Q 103 : # EmailAddress.where(:user_id => users.map(&:id)).where("is_default = ? OR notify = ?", true, true).pluck(:address)
EmailAddress
.where('user_id = ?')
.where("(is_default = true) || (notify = true)")
.select('address')
# Q 104 : # Enumeration.find(params[:id])
Enumeration
.where('id = ?')
# Q 105 : # Group.find(params[:id])
Group
.where('id = ?')
# Q 106 : # Group.givable.active.visible.where(:id => user_ids).to_a
Group
.where('id = ?')
# Q 107 : # Group.givable.active.visible.where(:id => user_ids).to_a
Group
.where('id = ?')
# Q 108 : # Group.givable.limit(100)
Group
.return_limit('100')
# Q 109 : # Group.named(group_name).first
Group
.return_limit('1')
# Q 110 : # Group.where(:id => value).to_a
Group
.where('id = ?')
# Q 111 : # Import.where(:user_id => User.current.id, :filename => params[:id]).first
Import
.where('user_id = ?')
.where('filename = ?')
.return_limit('1')
# Q 112 : # Issue.find(params[:id])
Issue
.where('id = ?')
# Q 113 : # Issue.find(params[:issue_id])
Issue
.where('id = ?')
# Q 114 : # Issue.find(params[:issue_id])
Issue
.where('id = ?')
# Q 115 : # Issue.find_by(:id => issue_id)
Issue
.where('id = ?')
# Q 116 : # Issue.find_by_id(child_id)
Issue
.where('id = ?')
# Q 117 : # Issue.find_by_id(detail.value || detail.old_value).try(:visible?, user)
Issue
.where('id = ?')
.joins('project')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 118 : # Issue.find_by_id(id.to_i)
Issue
.where('id = ?')
# Q 119 : # Issue.find_by_id(issue_id)
Issue
.where('id = ?')
# Q 120 : # Issue.find_by_id(m[1])
Issue
.where('id = ?')
# Q 121 : # Issue.joins("JOIN Issue ancestors" + " ON ancestors.root_id = Issue.root_id" + " AND ancestors.lft <= Issue.lft AND ancestors.rgt >= Issue.rgt").where(:ancestors => { :id => issues.map(&:id) })
# Q 122 : # Issue.joins(:project).where("Project.lft < ? OR Project.rgt > ?", lft, rgt).where(:fixed_version_id => version_ids).exists?
Issue
.joins('project')
.where('(project.lft < ?) || (project.rgt > ?)')
.where('fixed_version_id = ?')
.return_limit('1')
# Q 123 : # Issue.joins(:project, :fixed_version).where("Issue.fixed_version_id IS NOT NULL" + " AND Issue.project_id <> Version.project_id" + " AND Version.sharing <> 'system'").where(conditions).each
Issue
.joins('project')
.joins('fixed_version')
.where('fixed_version_id != 0')
.where('project_id != fixed_version.project_id')
.where("fixed_version.sharing <> 'system'")
# Q 124 : # Issue.open.where("Issue.assigned_to_id IS NOT NULL" + " AND Project.status = #{
# Project::STATUS_ACTIVE}" + " AND Issue.due_date <= ?", days.day.from_now.to_date)
Issue
.joins('project')
.where('assigned_to_id != 0')
.where('project.status = 1')
.where('due_date < ?')
# Q 125 : # Issue.self_and_descendants(@issues).pluck(:id)
Issue
.where('(id = param[id]) || (parent_id = param[id])')
.select('id')
# Q 126 : # Issue.visible(User.current, :project => options[:project], :with_subprojects => options[:with_subprojects]).joins(:status, assoc.name).group(:status_id, :is_closed, select_field).count.map
# Q 127 : # Issue.visible(user).find_by_id(issue_id)
Issue
.where('id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 128 : # Issue.visible.find(arg)
Issue
.where('id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 129 : # Issue.visible.find(params[:copy_from])
Issue
.where('id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 130 : # Issue.visible.find_by_id(detail.old_value)
Issue
.where('id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 131 : # Issue.visible.find_by_id(detail.value)
Issue
.where('id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 132 : # Issue.visible.find_by_id(m[1].to_i)
Issue
.where('id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 133 : # Issue.visible.find_by_id(oid)
Issue
.where('id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 134 : # Issue.visible.find_by_id(params[:issue_id])
Issue
.where('id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 135 : # Issue.visible.find_by_id(params[:issue_id])
Issue
.where('id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 136 : # Issue.visible.includes(:project, :tracker).preload(:status, :priority, :fixed_version).where(:tracker_id => @selected_tracker_ids, :project_id => project_ids, :fixed_version_id => @versions.map(&:id)).order("Project.lft, Tracker.position, Issue.id")
Issue
.includes('project')
.includes('tracker')
.includes('status')
.includes('priority')
.includes('fixed_version')
.where('tracker_id = ?')
.where('project_id = ?')
.where('fixed_version_id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
.order('project.lft, tracker.position, id')
# Q 137 : # Issue.visible.joins(:project).where(statement)
Issue
.joins('project')
# Q 138 : # Issue.visible.joins(:status, :project).preload(:priority).where(statement).includes((
# [:status, :project] + (
# options[:include] || [])).uniq).where(options[:conditions]).order(order_option).joins(joins_for_order_statement(order_option.join(","))).limit(options[:limit]).offset(options[:offset])
Issue
.joins('status')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
.includes('priority')
# Q 139 : # Issue.visible.joins(:status, :project).where(statement).includes((
# [:status, :project] + (
# options[:include] || [])).uniq).references((
# [:status, :project] + (
# options[:include] || [])).uniq).where(options[:conditions]).order(order_option).joins(joins_for_order_statement(order_option.join(","))).limit(options[:limit]).offset(options[:offset]).pluck(:id)
# Q 140 : # Issue.visible.open.where(:author_id => @user.id).count
Issue
.where('author_id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
# Q 141 : # Issue.visible.open.where(cond).group(:tracker).count
Issue
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
.group('tracker')
# Q 142 : # Issue.visible.where(:author_id => @user.id).count
Issue
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
.where('author_id = ?')
# Q 143 : # Issue.visible.where(:id => @unsaved_issues.map(&:id)).to_a
Issue
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
.where('id = ?')
# Q 144 : # Issue.visible.where(:project => User.current.projects).where("(start_date>=? and start_date<=?) or (due_date>=? and due_date<=?)", calendar.startdt, calendar.enddt, calendar.startdt, calendar.enddt).includes(:project, :tracker, :priority, :assigned_to).references(:project, :tracker, :priority, :assigned_to).to_a
Issue
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
.where('project_id = ?')
.where('((start_date >= ?) && (start_date <= ?)) ||((due_date >= ?) && (due_date <= ?))')
.includes('project')
.includes('tracker')
.includes('priority')
.includes('assigned_to')
# Q 145 : # Issue.visible.where(cond).group(:tracker).count
Issue
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
.group('tracker')
# Q 146 : # Issue.visible.where(cond).sum(:estimated_hours).to_f
# Q 147 : # Issue.where(:fixed_version_id => value.map(&:to_i)).pluck(:id)
Issue
.where('fixed_version_id = ?')
.select('id')
# Q 148 : # Issue.where(:id => (
# params[:id] || params[:ids])).preload(:project, :status, :tracker, :priority, :author, :assigned_to, :relations_to, { :custom_values => :custom_field }).to_a
Issue
.where('id = ?')
.includes('project')
.includes('status')
.includes('tracker')
.includes('priority')
.includes('author')
.includes('assigned_to')
.includes('relations_to')
# Q 149 : # Issue.where(:id => @issues.map(&:id)).to_a
Issue
.where('id = ?')
# Q 150 : # Issue.where(:id => child_ids).pluck(:parent_id).compact.uniq
Issue
.where('id IN (?, ?)')
.select('parent_id')
.where('id != 0')
.distinct('')
# Q 151 : # Issue.where(:id => object_ids).order(:id).preload(:tracker, :priority, :status)
Issue
.where('id IN (?, ?)')
.order('id')
.includes('tracker')
.includes('priority')
.includes('status')
# Q 152 : # Issue.where(:id => value.first.to_i).first
Issue
.where('id = ?')
.return_limit('1')
# Q 153 : # Issue.where(:id => value.first.to_i).pluck(:root_id, :lft, :rgt).first
Issue
.where('id = ?')
.select('root_id')
.select('lft')
.select('rgt')
.return_limit('1')
# Q 154 : # Issue.where(:id => value.first.to_i).pluck(:root_id, :lft, :rgt).first
Issue
.where('id = ?')
.select('root_id')
.select('lft')
.select('rgt')
.return_limit('1')
# Q 155 : # Issue.where(:parent_id => nil).find(root_id)
Issue
.where('parent_id = ?')
.where('id = ?')
# Q 156 : # Issue.where(:project_id => project.id)
Issue
.where('project_id = ?')
# Q 157 : # Issue.where(:status_id => id).any?
Issue
.where('status_id = ?')
# Q 158 : # Issue.where(:status_id => id, :closed_on => nil).update_all("closed_on = (#{
# subquery})")
Issue
.where('status_id = ?')
.where('closed_on = ?')
# Q 159 : # Issue.where(:status_id => id, :closed_on => nil).update_all("closed_on = created_on")
Issue
.where('status_id = ?')
.where('closed_on = ?')
# Q 160 : # Issue.where(:tracker_id => self.id).any?
Issue
.where('tracker_id = ?')
# Q 161 : # Issue.where(["assigned_to_id = ?", id]).update_all("assigned_to_id = NULL")
Issue
.where('assigned_to_id = ?')
# Q 162 : # Issue.where(["assigned_to_id = ?", id]).update_all("assigned_to_id = NULL")
Issue
.where('assigned_to_id = ?')
# Q 163 : # IssueCategory.where(["project_id = ? AND assigned_to_id = ?", project_id, user_id]).update_all("assigned_to_id = NULL")
IssueCategory
.where('project_id = ?')
.where('assigned_to_id = ?')
# Q 164 : # IssueCustomField.sorted.where("is_for_all = ? OR id IN (?)", true, issue_custom_field_ids)
IssueCustomField
.where('(is_for_all = true) || (id IN (?, ?, ?))')
# Q 165 : # IssueCustomField.where(:visible => false).joins(:roles).pluck(:id, "role_id").each
IssueCustomField
.where('visible = false')
.joins('roles')
.select('roles.id')
# Q 166 : # IssueCustomField.where(is_for_all: false).joins(:projects).group(:custom_field_id).count
# IssueCustomField
# .where('is_for_all = false')
# .joins('projects')
# .group('custom_field_id')
# Q 167 : # IssuePriority.active.named(priority_name).first.try(:id)
IssuePriority
.select('active')
.return_limit('1')
.select('id')
# Q 168 : # IssuePriority.find_by_position(priority_position)
IssuePriority
.where('position = ?')
# Q 169 : # IssueQuery.find_by_id(session_data[:id])
IssueQuery
.where('id = ?')
# Q 171 : # IssueQuery.visible.find_by_id(settings[:query_id])
IssueQuery
.where('id = ?')
# Q 172 : # IssueRelation.find(params[:id])
IssueRelation
.where('id = ?')
# Q 174 : # IssueRelation.where("issue_to_id = ? OR issue_from_id = ?", id, id).find(relation_id)
IssueRelation
.where('(issue_to_id = param[issue_id]) || (issue_from_id = param[issue_id])')
.where('id = ?')
# Q 175 : # IssueRelation.where(:issue_from_id => issue_ids, :issue_to_id => issue_ids, :relation_type => DRAW_TYPES.keys).group_by(&:issue_from_id)
IssueRelation
.where('issue_from_id = param[issue_id]')
.where('issue_to_id = param[issue_id]')
.where('relation_type = ?')
.group('issue_from_id')
# Q 176 : # IssueStatus.find(params[:id])
IssueStatus
.where('id = ?')
# Q 177 : # IssueStatus.find(params[:id])
IssueStatus
.where('id = ?')
# Q 178 : # IssueStatus.find(params[:id]).destroy
IssueStatus
.where('id = ?')
# Q 179 : # IssueStatus.find_by_id(s.to_i)
IssueStatus
.where('id = ?')
# Q 180 : # IssueStatus.find_by_id(status_id)
IssueStatus
.where('id = ?')
# Q 181 : # IssueStatus.find_by_id(status_id_was)
IssueStatus
.where('id = ?')
# Q 182 : # IssueStatus.find_by_id(status_id_was)
IssueStatus
.where('id = ?')
# Q 183 : # IssueStatus.joins(:workflow_transitions_as_new_status).where(:workflows => { :old_status_id => status_id, :role_id => roles.map(&:id), :tracker_id => tracker.id })
# Q 184 : # IssueStatus.named(status_name).first.try(:id)
IssueStatus
.return_limit('1')
.select('id')
# Q 185 : # IssueStatus.where("default_done_ratio >= 0").each
IssueStatus
.where('default_done_ratio >= 0')
# Q 186 : # IssueStatus.where(:id => issue_status_ids).sorted
IssueStatus
.where('id = ?')
# Q 187 : # IssueStatus.where(:id => issue_status_ids).to_a.sort
IssueStatus
.where('id = ?')
# Q 188 : # IssueStatus.where(:id => status_ids).sorted.to_a.presence
IssueStatus
.where('id = ?')
# Q 189 : # Journal.find_by(:id => journal_id)
Journal
.where('id = ?')
# Q 190 : # Journal.joins(:details).where(:journalized_type => "Issue").where("journalized_id = Issue.id").where(:journal_details => { :property => "attr", :prop_key => "status_id", :value => id.to_s }).select("MAX(created_on)").to_sql
Journal
.joins('details')
.where('journalized_type = ?')
.where('journalized_id = ?')
.where('details.value = ?')
.where('details.property = ?')
.select('created_on')
# Q 191 : # Journal.joins(issue: :project).where(:journalized_type => "Issue", :journalized_id => issue_ids).where(Journal.visible_notes_condition(user, :skip_pre_condition => true)).group(:journalized_id).maximum(:id).values
Journal
.where('journalized_type = ?')
.where('journalized_id = ?')
.group('journalized_id')
# Q 192 : # Journal.joins(issue: :project).where(:journalized_type => "Issue", :journalized_id => issue_ids).where(Journal.visible_notes_condition(user, :skip_pre_condition => true)).where.not(notes: "").group(:journalized_id).maximum(:id).values
Journal
.where('journalized_type = ?')
.where('journalized_id = ?')
.where('notes = ?')
.group('journalized_id')
# Q 193 : # Journal.visible.find(params[:id])
Journal
.joins('issue => project')
.where('issue.project.status != 3')
.where("exists(issue.project.enabled_modules, name = 'issue_tracking')")
.where('id = ?')
# Q 194 : # Journal.visible.find(params[:journal_id])
Journal
.where('id = ?')
# Q 195 : # Journal.visible.joins(:issue => [:project, :status]).where(statement).order(options[:order]).limit(options[:limit]).offset(options[:offset]).preload(:details, :user, { :issue => [:project, :author, :tracker, :status] }).to_a
Journal
.joins('issue')
.includes('details')
.includes('user')
# Q 196 : # Journal.where(:id => journal_ids).preload(:user).to_a
Journal
.where('id = ?')
.includes('user')
# Q 197 : # Journal.where(:id => journal_ids).to_a
Journal
.where('id = ?')
# Q 198 : # Member.find(params[:id])
Member
.where('id = ?')
# Q 199 : # Member.find_by_project_id_and_user_id(member.project_id, user.id)
Member
.where('project_id = ?')
.where('user_id = ?')
# Q 200 : # Member.find_by_project_id_and_user_id(project_id, principal_id)
Member
.where('project_id = ?')
.where('user_id = ?')
# Q 201 : # Member.joins(:project, :member_roles).where("Project.status <> 9").where("Member.user_id = ? OR (Project.is_public = ? AND Member.user_id = ?)", self.id, true, group_id).pluck(:user_id, :role_id, :project_id)
Query(Member)
.joins('project')
.joins('member_roles')
.where("(project.is_public = true) && (user_id = ?)")
.pred_or("user_id = ?")
.select('user_id')
.select('member_roles.role_id')
.select('project_id')
# Q 202 : # Member.where(:project_id => id).delete_all
Query(Member)
.where('project_id = ?')
# Q 203 : # MemberRole.find_by_id(inherited_from)
Query(MemberRole)
.where('id = ?')
# Q 204 : # MemberRole.joins(:member).where("Member.user_id = ? AND MemberRole.inherited_from IN (?)", user.id, member.member_role_ids).each(&:destroy)
Query(MemberRole)
.joins('member')
.where("member.user_id = ?")
.where("inherited_from IN (?, ?)")
# Q 205 : # MemberRole.new(:role => member_role.role, :inherited_from => member_role.id)
# Q 209 : # MemberRole.where(:inherited_from => id).destroy_all
Query(MemberRole)
.where('inherited_from = ?')
# Q 210 : # MemberRole.where(:member_id => membership_ids).to_a
Query(MemberRole)
.where('member_id IN (?, ?)')
# Q 211 : # Message.find_by(:id => message_id).root
Query(Message)
.where('id = ?')
.select('parent_id')
# Q 212 : # Message.visible.find_by_id(oid)
Query(Message)
.where('id = ?')
# Q 213 : # News.visible.find_by_id(oid)
Query(News)
.where('id = ?')
# Q 214 : # News.visible.find_by_id(params[:id])
Query(News)
.where('id = ?')
# Q 215 : # News.visible.where(:project => User.current.projects).limit(10).includes(:project, :author).references(:project, :author).order("News.created_on DESC").to_a
Query(News)
.where('project_id = ?')
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'news')")
.return_limit('10')
.includes('project')
.includes('author')
.order('created_on')
# Q 216 : # Principal.active.joins(:members => :roles).where(:type => types, :members => { :project_id => id }, :roles => { :assignable => true }).distinct.sorted
Query(Principal)
.joins('members => roles')
.where('type IN (?, ?)')
.where('members.project_id = ?')
.where('members.roles.assignable = ?')
.distinct('')
# Q 217 : # Principal.active.joins(:members).where("Member.project_id = ?", id).distinct
Query(Principal)
.joins('members')
.where('members.project_id = ?')
.distinct('')
# Q 218 : # Principal.find(params[:user_id])
Query(Principal)
.where('id = ?')
# Q 219 : # Principal.find(principal_id)
Query(Principal)
.where('id = ?')
# Q 220 : # Principal.find_by_id(assigned_to_id_was)
Query(Principal)
.where('id = ?')
# Q 221 : # Principal.find_by_id(previous_assigned_to_id)
Query(Principal)
.where('id = ?')
# Q 222 : # Principal.visible(user).find_by(:id => id)
Query(Principal)
.where('id = ?')
# Q 223 : # Principal.visible.where(:id => values).map
Query(Principal)
.where('id = ?')
# Q 224 : # Project.active.has_module(:repository).order("Project.identifier").preload(:repository).to_a
Query(Project)
.order('identifier')
.includes('repositories')
# Q 225 : # Project.allowed_to(:rename_wiki_pages).joins(:wiki).preload(:wiki).to_a
Query(Project)
.joins('wiki')
.includes('wiki')
# Q 226 : # Project.allowed_to(user, :log_time).order(:lft)
Query(Project)
.where('status = 1')
.where("exists(enabled_modules, name = 'time_logging')")
.order('lft')
# Q 227 : # Project.find(options[:project])
Query(Project)
.where('id = ?')
# Q 228 : # Project.find(options[:project_id])
Query(Project)
.where('id = ?')
# Q 229 : # Project.find(params[:id])
Query(Project)
.where('id = ?')
# Q 230 : # Project.find(params[:id])
Query(Project)
.where('id = ?')
# Q 231 : # Project.find(params[:id])
Query(Project)
.where('id = ?')
# Q 232 : # Project.find(params[:id])
Query(Project)
.where('id = ?')
# Q 233 : # Project.find(params[:project_id])
Query(Project)
.where('id = ?')
# Q 234 : # Project.find(params[:project_id])
Query(Project)
.where('id = ?')
# Q 235 : # Project.find(params[:project_id])
Query(Project)
.where('id = ?')
# Q 236 : # Project.find(parent_id)
Query(Project)
.where('id = ?')
# Q 237 : # Project.find(project)
Query(Project)
.where('id = ?')
# Q 238 : # Project.find(project)
Query(Project)
.where('id = ?')
# Q 239 : # Project.find(project_id)
Query(Project)
.where('id = ?')
# Q 240 : # Project.find(project_id)
Query(Project)
.where('id = ?')
# Q 241 : # Project.find_by_id(parent_id_param)
Query(Project)
.where('id = ?')
# Q 242 : # Project.find_by_id(project_id)
Query(Project)
.where('id = ?')
# Q 243 : # Project.find_by_identifier(default_project)
Query(Project)
.where('identifier = ?')
# Q 244 : # Project.find_by_identifier(get_keyword(:project))
Query(Project)
.where('identifier = ?')
# Q 245 : # Project.find_by_identifier(identifier)
Query(Project)
.where('identifier = ?')
# Q 246 : # Project.find_by_identifier(p).try(:id)
Query(Project)
.where('identifier = ?')
.select('id')
# Q 247 : # Project.find_by_identifier(project_identifier)
Query(Project)
.where('identifier = ?')
# Q 248 : # Project.find_by_name(identifier)
Query(Project)
.where('name = ?')
# Q 249 : # Project.find_by_name(project_identifier)
Query(Project)
.where('name = ?')
# Q 250 : # Project.includes(:attachments).references(:attachments).reorder(sort_clause).find(@project.id)
Query(Project)
.includes('attachments')
.where('id = ?')
# Q 251 : # Project.order("id DESC").first
Query(Project)
.order('id')
.return_limit('1')
# Q 252 : # Project.visible(self).pluck(:id)
Query(Project)
.where('status != 3')
.select('id')
# Q 253 : # Project.visible.find_by_id(oid)
Query(Project)
.where('status != 3')
.where('id = ?')
# Q 254 : # Project.visible.find_by_identifier(project_identifier)
Query(Project)
.where('identifier = ?')
# Q 255 : # Project.visible.find_by_param(params[:project_id])
Query(Project)
.where('status != 3')
.where('id = ?')
# Q 256 : # Project.visible.joins("LEFT JOIN Project child ON Project.lft <= child.lft AND Project.rgt >= child.rgt").where("child.id IN (?)", ids).order("Project.lft ASC").distinct.to_a
Query(Project)
.where('status != 3')
.order('id, lft')
.distinct('')
# Q 257 : # Project.where(:default_version_id => id).update_all(:default_version_id => nil)
Query(Project)
.where('default_version_id = ?')
# Q 258 : # Project.where(:id => attributes["project_id"]).to_a
Query(Project)
.where('id = ?')
# Q 259 : # Project.where(:id => id).pluck(:lft, :rgt).first
Query(Project)
.where('id = ?')
.select('lft')
.select('rgt')
.return_limit('1')
# Q 260 : # Project.where(:id => ids).to_a
Query(Project)
.where('id = ?')
# Q 261 : # Project.where(:parent_id => parent_id).where(:rgt => nil, :lft => nil).reorder(:name)
Query(Project)
.where('parent_id = ?')
.where('rgt = 0')
.where('lft = 0')
.order('name')
# Q 262 : # Project.where(default_assigned_to: self).update_all(default_assigned_to_id: nil)
Query(Project)
.where('default_assigned_to_id = ?')
# Q 263 : # Project.where(id: bookmarked_project_ids).visible
Query(Project)
.where('id = ?')
# Q 264 : # Project.where(id: project_ids)
Query(Project)
.where('id IN (?, ?)')
# Q 265 : # Query.find(params[:id])
# Q 266 : # QueryColumn.new(:is_private, :sortable => "Issue.is_private", :groupable => true)
# Q 267 : # Repository.find(params[:id])
Query(Repository)
.where('id = ?')
# Q 268 : # Repository.where(:project_id => project.id).empty?
Query(Repository)
.where('project_id = ?')
# Q 269 : # Role.all.select(&:consider_workflow?)
Query(Role)
.where('permissions = ?')
# Q 270 : # Role.all.select(&:consider_workflow?).map(&:id)
Query(Role)
.where('permissions = ?')
#Q 271 : # Role.find(params[:id])
Query(Role)
.where('id = ?')
# Q 272 : # Role.find_by_id(arg.to_s)
Query(Role)
.where('id = ?')
# Q 273 : # Role.find_by_id(params[:copy])
Query(Role)
.where('id = ?')
# Q 274 : # Role.find_by_id(params[:copy_workflow_from])
Query(Role)
.where('id = ?')
# Q 275 : # Role.find_by_id(params[:source_role_id].to_i)
Query(Role)
.where('id = ?')
# Q 276 : # Role.givable.find_by_id(Setting.new_project_user_role_id.to_i)
Query(Role)
.where('builtin = 0')
.where('id = ?')
.order('position')
# Q 277 : # Role.sorted.select(&:consider_workflow?)
Query(Role)
.where('permissions = ?')
.order('builtin, position')
# Q 278 : # Role.sorted.select(&:consider_workflow?)
Query(Role)
.where('permissions = ?')
.order('builtin, position')
# Q 279 : # Role.sorted.select(&:consider_workflow?)
Query(Role)
.where('permissions = ?')
.order('builtin, position')
# Q 280 : # Role.where(:assignable => true).select
Query(Role)
.where('assignable = true')
# Q 281 : # Role.where(:builtin => 0).exists?
Query(Role)
.where('builtin = 0')
.return_limit('1')
# Q 282 : # Role.where(:id => hash.keys).to_a
Query(Role)
.where('id IN (?, ?)')
# Q 283 : # Role.where(:id => ids).to_a
Query(Role)
.where('id IN (?, ?)')
# Q 284 : # Role.where(:id => params[:permissions].keys)
Query(Role)
.where('id = ?')
# Q 285 : # Role.where(:id => params[:target_role_ids]).to_a
Query(Role)
.where('id = ?')
# Q 286 : # Setting.mail_handler_body_delimiters.to_s.split(/[\r\n]+/).reject(&:blank?)
# Q 287 : # TimeEntry.find(params[:id])
Query(TimeEntry)
.where('id = ?')
# Q 288 : # TimeEntry.joins(:issue).where("Issue.fixed_version_id = ?", id).sum(:hours).to_f
Query(TimeEntry)
.joins('issue')
# Q 289 : # TimeEntry.visible(user).joins(:issue).joins("JOIN Issue parent ON parent.root_id = Issue.root_id" + " AND parent.lft <= Issue.lft AND parent.rgt >= Issue.rgt").where("parent.id IN (?)", issues.map(&:id)).group("parent.id").sum(:hours)
# Query(TimeEntry)
# .joins('issue')
# .group('id')
# cannot handle joining on one table multiple times...
# Q 290 : # TimeEntry.visible(user).where(:issue_id => issues.map(&:id)).group(:issue_id).sum(:hours)
Query(TimeEntry)
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'time_tracking')")
.where('issue_id IN (?, ?)')
.group('issue_id')
# Q 291 : # TimeEntry.visible.joins(:project, :user).includes(:activity).references(:activity).left_join_issue.where(statement)
Query(TimeEntry)
.joins('project')
.joins('user')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'time_tracking')")
.includes('activity')
# Q 292 : # TimeEntry.visible.where(cond).sum(:hours).to_f
Query(TimeEntry)
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'time_tracking')")
# Q 293 : # TimeEntry.where("TimeEntry.user_id = ? AND TimeEntry.spent_on BETWEEN ? AND ?", User.current.id, User.current.today - (
# days - 1), User.current.today).joins(:activity, :project).references(:issue => [:tracker, :status]).includes(:issue => [:tracker, :status]).order("TimeEntry.spent_on DESC, Project.name ASC, Tracker.position ASC, Issue.id ASC").to_a
Query(TimeEntry)
.where("user_id = ?")
.where("spent_on > ?")
.where("spent_on < ?")
.joins('activity')
.joins('project')
.includes('issue => tracker')
.includes('issue => status')
.order('spent_on, project.name, issue.tracker.position, issue.id')
# Q 294 : # TimeEntry.where(:activity_id => self_and_descendants(1).map(&:id))
Query(TimeEntry)
.where('activity_id = ?')
# Q 295 : # TimeEntry.where(:id => params[:id] || params[:ids]).preload(:project => :time_entry_activities).preload(:user).to_a
Query(TimeEntry)
.where('id = ?')
.includes('project => time_entry_activities')
.includes('user')
# Q 296 : # TimeEntry.where(:id => params[:ids]).preload(:project => :time_entry_activities).preload(:user).to_a
Query(TimeEntry)
.where('id = ?')
.includes('project => time_entry_activities')
# Q 297 : # TimeEntry.where(:id => saved_items.pluck(:obj_id)).order(:id).preload(:activity, :project, :issue => [:tracker, :priority, :status])
Query(TimeEntry)
.where('id = ?')
.order('id')
.includes('activity')
.includes('project')
.includes('issue')
# Q 298 : # TimeEntry.where(:id => unsaved_time_entries.map(&:id)).preload(:project => :time_entry_activities).preload(:user).to_a
Query(TimeEntry)
.where('id = ?')
.includes('project => time_entry_activities')
# Q 299 : # TimeEntry.where(:issue_id => issues_and_descendants_ids)
Query(TimeEntry)
.where('issue_id = ?')
# Q 300 : # TimeEntry.where(:user_id => user_id, :spent_on => spent_on).where.not(:id => id).sum(:hours).to_f
Query(TimeEntry)
.where('user_id = ?')
.where('spent_on = ?')
.where('id != ?')
# Q 301 : # TimeEntryActivity.find(activity["parent_id"])
Query(TimeEntryActivity)
.where('id = ?')
# Q 302 : # TimeEntryActivity.where("#{
# t}.project_id IS NULL OR #{
# t}.project_id = ?", id)
Query(TimeEntryActivity)
.where("project_id = 0")
.pred_or('project_id = ?')
# Q 316 : # Tracker.find(options[:tracker])
Query(Tracker)
.where('id = ?')
# Q 317 : # Tracker.find(params[:id])
Query(Tracker)
.where('id = ?')
# Q 318 : # Tracker.find(params[:id])
Query(Tracker)
.where('id = ?')
# Q 319 : # Tracker.find(params[:id])
Query(Tracker)
.where('id = ?')
# Q 320 : # Tracker.find_by_id(params[:copy_workflow_from])
Query(Tracker)
.where('id = ?')
# Q 321 : # Tracker.find_by_id(params[:source_tracker_id].to_i)
Query(Tracker)
.where('id = ?')
# Q 322 : # Tracker.find_by_id(tracker_id)
Query(Tracker)
.where('id = ?')
# Q 323 : # Tracker.find_by_id(tracker_id)
Query(Tracker)
.where('id = ?')
# Q 324 : # Tracker.find_by_id(tracker_id_in_database)
Query(Tracker)
.where('id = ?')
# Q 325 : # Tracker.joins(projects: :enabled_modules).where("Project.status <> ?", STATUS_ARCHIVED).where(:enabled_modules => { :name => "issue_tracking" }).distinct.sorted
Query(Tracker)
.joins("projects => enabled_modules")
.where('projects.status != 3')
.where("projects.enabled_modules.name = 'issue_tracking'")
.distinct('')
# Q 326 : # Tracker.new(:default_status => IssueStatus.sorted.first)
# Q 327 : # Tracker.where(:default_status_id => id).any?
Query(Tracker)
.where('default_status_id = ?')
# Q 328 : # Tracker.where(:id => default.map(&:to_i)).sorted.to_a
Query(Tracker)
.where('id = ?')
# Q 329 : # Tracker.where(:id => ids).to_a
Query(Tracker)
.where('id IN (?, ?)')
# Q 330 : # Tracker.where(:id => params[:target_tracker_ids]).to_a
Query(Tracker)
.where('id IN (?, ?)')
# Q 331 : # Tracker.where(:id => tracker_id_was, :default_status_id => status_id_was).any?
Query(Tracker)
.where('id = ?')
.where('default_status_id = ?')
# Q 332 : # User.active.admin.where("id <> ?", id).exists?
Query(User)
.where("id != ?")
.select('admin')
.return_limit('1')
# Q 333 : # User.active.find(params[:user_id])
Query(User)
.where("type = 'User'")
.where('id = ?')
# Q 334 : # User.active.find(session[:user_id])
Query(User)
.where("type = 'User'")
.where('id = ?')
# Q 335 : # User.active.find_by_login("admin").try(:check_password?, "admin")
Query(User)
.where("type = 'User'")
.where('login = ?')
.select('admin')
# Q 336 : # User.active.having_mail(addresses).to_a
Query(User)
.where("type = 'User'")
.where('exists(email_addresses, address = ?)')
# Q 337 : # User.active.joins(:members).where("Member.project_id = ?", id).distinct
Query(User)
.joins('members')
.where("members.project_id = ?")
.distinct('')
# Q 338 : # User.active.sorted.not_in_group(group).like(params[:q])
Query(User)
.where("type = 'User'")
# Q 339 : # User.active.visible.where(:id => user_ids).to_a
Query(User)
.where("type = 'User'")
.where('status = 1')
.where('id = ?')
# Q 340 : # User.active.visible.where(:id => user_ids).to_a
Query(User)
.where("type = 'User'")
.where('status = 1')
.where('id IN (?, ?)')
# Q 341 : # User.active.where(:admin => true)
Query(User)
.where("type = 'User'")
.where('admin = true')
# Q 342 : # User.active.where(admin: true).to_a
Query(User)
.where("type = 'User'")
.where('admin = true')
# Q 343 : # User.active.where(admin: true).to_a
Query(User)
.where("type = 'User'")
.where('admin = true')
# Q 344 : # User.current.allowed_to?(:copy_issues, @copy_from.project)
# Q 346 : # User.find(params[:id])
Query(User)
.where('id = ?')
# Q 347 : # User.find(params[:user_id])
Query(User)
.where('id = ?')
# Q 348 : # User.find_by_api_key(key)
# Query(User)
# .where('api_key = ?')
# # Q 349 : # User.find_by_api_key(username)
# Query(User)
# .where('api_key = ?')
# Q 350 : # User.find_by_id(user_id)
Query(User)
.where('id = ?')
# Q 351 : # User.find_by_login(username)
Query(User)
.where('login = ?')
# Q 352 : # User.find_by_login(username)
Query(User)
.where('login = ?')
# Q 353 : # User.find_by_mail(email)
Query(User)
.joins("email_addresses")
.where('exists(email_addresses, address = ?)')
# Q 354 : # User.find_by_mail(email)
Query(User)
.joins("email_addresses")
.where('exists(email_addresses, address = ?)')
# Q 355 : # User.find_by_mail(sender_email)
Query(User)
.joins("email_addresses")
.where('exists(email_addresses, address = ?)')
# Q 356 : # User.find_by_rss_key(params[:key])
# Query(User)
# .where('rss_key = ?')
# Q 357 : # User.group("status").count.to_hash
Query(User)
.group('status')
# Q 358 : # User.joins(:groups).group("group_id").count
Query(User)
.joins('groups')
.group('groups.group_id')
# Q 359 : # User.logged.find(params[:id])
Query(User)
.where('id = ?')
# Q 360 : # User.logged.status(@status).preload(:email_address)
Query(User)
.select('status')
.includes('email_address')
# Q 361 : # User.not_in_group(@group).where(:id => (
# params[:user_id] || params[:user_ids])).to_a
Query(User)
.where('id = ?')
# Q 362 : # User.visible.find_by("LOWER(login) = :s AND type = 'User'", :s => name.downcase)
Query(User)
.where("type = 'User'")
.where("login = ?")
# Q 363 : # User.visible.find_by("LOWER(login) = :s AND type = 'User'", :s => name.downcase)
Query(User)
.where("type = 'User'")
.where("login = ?")
# Q 364 : # User.visible.find_by(:id => oid, :type => "User")
Query(User)
.where('id = ?')
.where("type = 'User'")
# Q 365 : # User.where("id IN (SELECT DISTINCT user_id FROM #{
# table_name})").each
# Q 366 : # User.where("salt IS NULL OR salt = ''").find_each
Query(User)
.where("salt = NULL")
.pred_or("salt = ''")
# Q 367 : # User.where(:id => additional_user_ids).to_a
Query(User)
.where('id = ?')
# Q 368 : # User.where(:id => user.id).update_all(:salt => salt, :hashed_password => hashed_password)
Query(User)
.where('id = ?')
# Q 369 : # User.where(:id => user_ids).inject({ })
Query(User)
.where('id = ?')
# Q 370 : # Version.joins(:project).preload(:project).where("Project.id = #{
# id}" + " OR (Project.status <> #{
# Project::STATUS_ARCHIVED} AND (" + " Version.sharing = 'system'" + " OR (Project.lft >= #{
# r.lft} AND Project.rgt <= #{
# r.rgt} AND Version.sharing = 'tree')" + " OR (Project.lft < #{
# lft} AND Project.rgt > #{
# rgt} AND Version.sharing IN ('hierarchy', 'descendants'))" + " OR (Project.lft > #{
# lft} AND Project.rgt < #{
# rgt} AND Version.sharing = 'hierarchy')" + "))")
Version
.joins('project')
.where('project.id = ?')
.pred_or("(project.status != 3) AND ((project.lft >= param[lft]) AND ((project.rgt <= param[rgt]) AND (sharing = 'system')))")
.pred_or("(project.status != 3) AND ((project.lft < param[lft]) AND ((project.rgt > param[rgt]) AND (sharing = 'hierarchy')))")
.pred_or("(project.status != 3) AND ((project.lft > param[lft]) AND ((project.rgt < param[rgt]) AND (sharing = 'hierarchy')))")
.includes('project')
# Q 371 : # Version.joins(:project).preload(:project).where("Project.status <> ? AND Version.sharing = 'system'", STATUS_ARCHIVED)
Query(Version)
.joins('project')
.where('project.status != 3')
.where("sharing = 'system'")
.includes('project')
# Q 372 : # Version.joins(:project).where("Project.lft >= ? AND Project.rgt <= ? AND Project.status <> ?", lft, rgt, STATUS_ARCHIVED)
Query(Version)
.joins('project')
.where('project.lft >= ?')
.where('project.rgt <= ?')
.where('project.status != 3')
# Q 373 : # Version.named(options[:version]).pluck(:id)
Query(Version)
.where("name = ?")
.select('id')
# Q 374 : # Version.visible.find_by_id(oid)
Query(Version)
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
.where('id = ?')
# Q 375 : # Version.visible.where(project_statement).where(options[:conditions]).includes(:project).references(:project).to_a
Query(Version)
.joins('project')
.where('project.status != 3')
.where("exists(project.enabled_modules, name = 'issue_tracking')")
.includes('project')
# Q 376 : # Version.where(:id => custom_value.value).to_a
Query(Version)
.where('id = ?')
# Q 377 : # Watcher.where("user_id = ?", id).delete_all
Query(Watcher)
.where('user_id = ?')
# Q 378 : # Watcher.where("user_id = ?", id).delete_all
Query(Watcher)
.where('user_id = ?')
# Q 379 : # Watcher.where(:watchable_type => "Issue", :watchable_id => @issues.map(&:id)).exists?
Query(Watcher)
.where("watchable_type = 'Issue'")
.where('watchable_id = ?')
.return_limit('1')
# Q 380 : # Watcher.where(:watchable_type => base_class.name, :watchable_id => objects.map(&:id), :user_id => user.id).exists?
Query(Watcher)
.where('watchable_type = ?')
.where('watchable_id = ?')
.where('user_id = ?')
.return_limit('1')
# Q 381 : # Wiki.find_by_id(redirects_to_wiki_id)
Query(Wiki)
.where('id = ?')
# Q 382 : # Wiki.find_by_id(w_id)
Query(Wiki)
.where('id = ?')
# Q 383 : # WikiContentVersion.reorder(version: :asc).includes(:author).where("wiki_content_id = ? AND version > ?", wiki_content_id, version).first
Query(WikiContentVersion)
.order('version')
.includes('author')
.return_limit('1')
# Q 384 : # WikiContentVersion.reorder(version: :desc).includes(:author).where("wiki_content_id = ? AND version < ?", wiki_content_id, version).first
Query(WikiContentVersion)
.where('wiki_content_id = ?')
.where('version = ?')
.order('version')
.includes('author')
.return_limit('1')
# Q 385 : # WikiPage.where(:id => child.id)
Query(WikiPage)
.where('id = ?')
# Q 386 : # WikiRedirect.where(:redirects_to => title_was, :redirects_to_wiki_id => wiki_id_was).each
Query(WikiRedirect)
.where('redirects_to = ?')
.where('redirects_to_wiki_id = ?')
# Q 387 : # WikiRedirect.where(:redirects_to_wiki_id => id).delete_all
Query(WikiRedirect)
.where('redirects_to_wiki_id = ?')
# Q 388 : # WikiRedirect.where(:redirects_to_wiki_id => wiki_id, :redirects_to => title).delete_all
Query(WikiRedirect)
.where('redirects_to_wiki_id = ?')
.where('redirects_to = ?')
# Q 389 : # WikiRedirect.where(:wiki_id => id).delete_all
Query(WikiRedirect)
.where('wiki_id = ?')
# Q 390 : # WikiRedirect.where(:wiki_id => wiki_id, :title => title).delete_all
Query(WikiRedirect)
.where('wiki_id = ?')
.where('title = ?')
# Q 391 : # WorkflowPermission.where(:tracker_id => tracker_id, :old_status_id => status_id, :role_id => roles.map(&:id)).to_a
Query(WorkflowPermission)
.where('tracker_id = ?')
.where('old_status_id = ?')
.where('role_id = ?')
# Q 392 : # WorkflowPermission.where(:tracker_id => trackers.map(&:id), :role_id => roles.map(&:id)).inject({ })
Query(WorkflowPermission)
.where('tracker_id = ?')
.where('role_id = ?')
# Q 393 : # WorkflowRule.where(:new_status_id => id).delete_all
Query(WorkflowRule)
.where('new_status_id = ?')
# Q 394 : # WorkflowRule.where(:old_status_id => id).delete_all
Query(WorkflowRule)
.where('old_status_id = ?')
# Q 395 : # WorkflowTransition.group(:tracker_id, :role_id).count
Query(WorkflowTransition)
.group('tracker_id, role_id')
# Q 396 : # WorkflowTransition.where(:role_id => @roles.map(&:id), :tracker_id => @trackers.map(&:id)).preload(:old_status, :new_status)
Query(WorkflowTransition)
.where('role_id = ?')
.where('tracker_id = ?')
.includes('old_status')
.includes('new_status')
# Q 397 : # WorkflowTransition.where(:tracker_id => @trackers.map(&:id), :role_id => role_ids).distinct.pluck(:old_status_id, :new_status_id).flatten.uniq
Query(WorkflowTransition)
.where('tracker_id = ?')
.where('role_id = ?')
.distinct('')
.select('old_status_id')
.select('new_status_id')
.distinct('')
# Q 398 : # WorkflowTransition.where(:tracker_id => id).distinct.pluck(:old_status_id, :new_status_id).flatten.uniq
Query(WorkflowTransition)
.where('tracker_id = ?')
.distinct('')
.select('old_status_id')
.select('new_status_id')
.distinct('')
# Q 399 : # WorkflowTransition.where(:tracker_id => rolled_up_trackers.map(&:id)).distinct.pluck(:old_status_id, :new_status_id).flatten.uniq
Query(WorkflowTransition)
.where('tracker_id = ?')
.distinct('')
.select('old_status_id')
.select('new_status_id')
.distinct('')
# Q 400 : # WorkflowTransition.where(:tracker_id => trackers.map(&:id), :role_id => roles.map(&:id)).to_a
Query(WorkflowTransition)
.where("tracker_id = ?")
.where("role_id = ?")
# Q 401 : # attachments.map(&:last)
Query(Attachment)
.return_limit("1")
# Q 402 : # attachments.select(&:readable?)
# Q 403 : # attachments.where(:id => deleted_attachment_ids.map(&:to_i))
Query(Attachment)
.where("id = ?")
# Q 404 : # attachments.where(:id => deleted_attachment_ids.map(&:to_i))
Query(Attachment)
.where("id = ?")
# Q 406 : # boards.select { |board|
#   
#   board.parent_id == parent_id
# }.sort_by(&:position).each
Query(Board)
.where('project_id = ?')
.where('parent_id != ?')
# Q 407 : # changesets.find_by(:revision => name.to_s)
Query(Changeset)
.where("revision = ?")
# Q 408 : # changesets.find_by(:revision => s)
Query(Changeset)
.where("revision = ?")
# Q 409 : # changesets.find_by(:revision => s)
Query(Changeset)
.where("revision = ?")
# Q 410 : # changesets.find_by_revision(identifier)
Query(Changeset)
.where("revision = ?")
# Q 411 : # changesets.find_by_revision(identifier)
Query(Changeset)
.where("revision = ?")
# Q 412 : # changesets.find_by_revision(identifier)
Query(Changeset)
.where("revision = ?")
# Q 413 : # changesets.find_by_revision(identifier)
Query(Changeset)
.where("revision = ?")
# Q 414 : # changesets.find_by_revision(rev)
Query(Changeset)
.where("revision = ?")
# Q 415 : # changesets.find_by_revision(rev_to)
Query(Changeset)
.where("revision = ?")
# Q 416 : # changesets.includes(:user).where(latest_changesets_cond(path, rev, limit)).references(:user).limit(limit).order("Changeset.id DESC").to_a
Query(Changeset)
.includes('user')
.return_limit('10')
.order('id')
# Q 417 : # changesets.map(&:user_id).compact.uniq
Query(Changeset)
.select('user_id')
.where("id != 0")
.distinct('')
# Q 418 : # changesets.reorder("Changeset.committed_on DESC, Changeset.id DESC").limit(limit).preload(:user).to_a
Query(Changeset)
.order('committed_on, id')
.return_limit('10')
.includes('user')
# Q 419 : # changesets.where("revision LIKE ?", s + "%").first
Query(Changeset)
.where("revision = ?")
.return_limit('1')
# Q 420 : # changesets.where("scmid LIKE ?", "#{
# name}%").first
Query(Changeset)
.where("scmid = ?")
.return_limit('1')
# Q 421 : # changesets.where("scmid LIKE ?", "#{
# s}%").first
Query(Changeset)
.where("scmid = ?")
.return_limit('1')
# Q 422 : # changesets.where(:committed_on => (
# tmp_time - time_delta)..(
# tmp_time + time_delta), :committer => author_utf8, :comments => cmt).first
Query(Changeset)
.where("committed_on = ?")
.where("committer = ?")
.where("comments = ?")
.return_limit('1')
# Q 423 : # changesets.where(:committer => committer).includes(:user).references(:user).first
Query(Changeset)
.where("committer = ?")
.includes('user')
.return_limit('1')
# Q 424 : # changesets.where(:revision => identifiers).includes(:user, :repository).group_by(&:revision)
Query(Changeset)
.where("revision = ?")
.includes('user')
.includes('repository')
.group('revision')
# Q 425 : # changesets.where(:revision => identifiers).reorder("committed_on DESC").includes(:repository, :user).to_a
Query(Changeset)
.where("revision = ?")
.order('committed_on')
.includes('repository')
.includes('user')
# Q 426 : # changesets.where(:scmid => revisions.map { |c|
#   
#   c.scmid
# }).to_a
Query(Changeset)
.where("scmid = ?")
# Q 427 : # changesets.where(:scmid => s).first
Query(Changeset)
.where("scmid = ?")
.return_limit('1')
# Q 428 : # changesets.where(:scmid => scmids)
Query(Changeset)
.where("scmid = ?")
# Q 429 : # custom_field.custom_values.where(:value => id.to_s)
Query(CustomValue)
.where("custom_field_id = ?")
.where("value = ?")
# Q 430 : # custom_field.enumerations.find_by_id(enumeration_id)
Query(CustomFieldEnumeration)
.where("custom_field_id = ?")
.where("id = ?")
# Q 431 : # custom_field.enumerations.where("LOWER(name) LIKE LOWER(?)", k).first.try(:id)
Query(CustomFieldEnumeration)
.where("name = ?")
.where("custom_field_id = ?")
.return_limit('1')
.select('id')
# Q 432 : # custom_field_values.select(&:visible?)
# Q 433 : # custom_values.where("EXISTS(SELECT 1 FROM CustomValue cve WHERE cve.custom_field_id = CustomValue.custom_field_id" + " AND cve.customized_type = CustomValue.customized_type AND cve.customized_id = CustomValue.customized_id" + " AND cve.id > CustomValue.id)").pluck(:id)
# Q 434 : # custom_values.where(:id => ids).delete_all
Query(CustomValue)
.where("id = ?")
# Q 435 : # documents.group_by(&:category)
Query(Document)
.where('project_id = ?')
.group('category_id')
# Q 436 : # editable_custom_field_values(user).map(&:custom_field).uniq
# Q 438 : # email_addresses.pluck(:address)
Query(EmailAddress)
.where('user_id = ?')
.select('address')
# Q 439 : # enabled_modules.pluck(:name)
Query(EnabledModule)
.where('project_id = ?')
.select('name')
# Q 440 : # find_by("LOWER(login) = ?", login.downcase)
Query(User)
.where('login = ?')
# Q 441 : # group.users
Query(User)
.joins('groups')
.where('groups.id = ?')
# Q 442 : # groups.inject([]) { |user_ids, group|
#   
#   user_ids + group.user_ids + [group.id]
# }.uniq.compact.sort.collect(&:to_s)
# Q 443 : # having_mail(mail).first
Query(User)
.where('exists(email_addresses, address = ?)')
.return_limit('1')
# Q 444 : # includes(:member_roles, :roles, :principal).reorder("Role.position").order(Principal.fields_for_order_statement)
Query(Member)
.includes('member_roles')
.includes('roles')
.includes('user')
.order('roles.position')
# Q 445 : # includes(:project).reorder("Project.lft")
Query(Member)
.joins('project')
.order('project.lft')
# Q 448 : # issue.project.issue_categories.named(category_name).first
Query(IssueCategory)
.where("id = ?")
.where("project_id = ?")
.return_limit('1')
# Q 449 : # issue.project.shared_versions.named(version_name).first
Version
.joins('project')
.where('project.id = ?')
.where('name = ?')
.pred_or("(project.status != 3) AND ((project.lft >= param[lft]) AND ((project.rgt <= param[rgt]) AND (sharing = 'system')))")
.pred_or("(project.status != 3) AND ((project.lft < param[lft]) AND ((project.rgt > param[rgt]) AND (sharing = 'hierarchy')))")
.pred_or("(project.status != 3) AND ((project.lft > param[lft]) AND ((project.rgt < param[rgt]) AND (sharing = 'hierarchy')))")
.return_limit("1")
# Q 450 : # issue.project.versions.named(version_name).first
Version
.joins('project')
.where('project.id = ?')
.where('name = ?')
.pred_or("(project.status != 3) AND ((project.lft >= param[lft]) AND ((project.rgt <= param[rgt]) AND (sharing = 'system')))")
.pred_or("(project.status != 3) AND ((project.lft < param[lft]) AND ((project.rgt > param[rgt]) AND (sharing = 'hierarchy')))")
.pred_or("(project.status != 3) AND ((project.lft > param[lft]) AND ((project.rgt < param[rgt]) AND (sharing = 'hierarchy')))")
.return_limit("1")
# Q 451 : # issue.relations_from.each
Query(IssueRelation)
.where("issue_from_id = ?")
# Q 452 : # issue.watcher_users.select { |u|
#   
#   u.status == User::STATUS_ACTIVE
# }.map(&:id)
Query(Watcher)
.where('watchable_id = ?')
.where('watchable_type = ?')
.joins('user')
.where('user.status = 1')
# Q 453 : # issues.collect(&:project).uniq.collect(&:id)
Query(Issue)
.select('project_id')
.distinct('')
# Q 454 : # issues.group_by(&:fixed_version)
Query(Issue)
.group('fixed_version_id')
# Q 455 : # issues.group_by(&:project)
Query(Issue)
.group('project_id')
# Q 456 : # issues.reject(&:leaf?).map { |issue|
#   
#   issue.descendants.ids
# }.flatten.uniq
# Q 457 : # joins("LEFT OUTER JOIN Issue ON Issue.id = TimeEntry.issue_id")
Query(TimeEntry)
.left_outer_joins('issue')
# Q 458 : # joins("LEFT OUTER JOIN Project ON #{
# table_name}.project_id = Project.id").where("#{
# table_name}.project_id IS NULL OR (#{
# base})")
# Q 459 : # joins(:board => :project).where(Project.allowed_to_condition(args.shift || User.current, :view_messages, *args))
Query(Board)
.joins('project')
.where("exists(project.enabled_modules, name = 'board')")
.where('project.status != 3')
# Q 460 : # joins(:issue => :project).where(Issue.visible_condition(user, options)).where(Journal.visible_notes_condition(user, :skip_pre_condition => true))
Query(Journal)
.joins('issue => project')
.where("exists(issue.project.enabled_modules, name = 'board')")
.where('issue.project.status != 3')
# Q 461 : # joins(:issue).where("Issue.root_id = #{
# issue.root_id} AND Issue.lft >= #{
# issue.lft} AND Issue.rgt <= #{
# issue.rgt}")
Query(TimeEntry)
.joins('issue')
.where("issue.root_id = ?")
.where("issue.lft >= ?")
.where("issue.rgt <= ?")
# Q 462 : # joins(:principal).where(:users => { :status => Principal::STATUS_ACTIVE })
Query(Member)
.joins('user')
.where("user.status = ?")
# Q 463 : # joins(:project).where(:projects => { :status => Project::STATUS_ACTIVE })
Query(Issue)
.joins('project')
.where("project.status = ?")
# Q 464 : # joins(:repository => :project).where(Project.allowed_to_condition(args.shift || User.current, :view_changesets, *args))
Query(Repository)
.joins('project')
.where("exists(project.enabled_modules, name = 'board')")
.where('project.status != 3')
# Q 465 : # joins(:status).where(:issue_statuses => { :is_closed => is_closed })
Query(Issue)
.joins('status')
.where("status.is_closed = ?")
# Q 466 : # journal.details.select { |d|
#   
#   d.property == "attachment" && d.value.present?
# }.map(&:prop_key)
# Q 467 : # journals.map(&:details).flatten.select { |d|
#   
#   d.property == "cf"
# }.map(&:prop_key).uniq
Query(Journal)
.joins("details")
.where("details.property = 'cf'")
.select('details.prop_key')
.distinct('')
# Q 468 : # journals.preload(:details).preload(:user => :email_address).reorder(:created_on, :id).to_a
Query(Journal)
.includes('details')
.includes('user => email_addresses')
.order('created_on, id')
# Q 469 : # journals.reorder("Journal.id ASC")
Query(Journal)
.where('issue_id = ?')
.order('id')
# Q 470 : # journals.reorder(:id => :desc).first.try(:user)
Query(Journal)
.where('issue_id = ?')
.order('id')
.return_limit('1')
.select('user_id')
# Q 471 : # journals.where.not(notes: "").reorder(:id => :desc).first.try(:notes)
Query(Journal)
.where('issue_id = ?')
.where("notes != ?")
.order('id')
.return_limit('1')
.select('notes')
# Q 472 : # member.role_inheritance(role).map do |h|
#   
#   if h.is_a?(Project)
#     
#     l(:label_inherited_from_parent_project)
#   elsif h.is_a?(Group)
#     
#     l(:label_inherited_from_group, :name => h.name.to_s)
#   end
#   
# end.compact.uniq
# Q 473 : # member_role.inherited_from
# Q 474 : # member_roles.select { |mr|
#   
#   !mr.inherited_from.nil?
# }.collect(&:role_id)
Query(MemberRole)
.where('member_id = ?')
.where('inherited_from = 0')
.select('role_id')
# Q 475 : # member_roles.select { |mr|
#   
#   mr.role_id == role.id && mr.inherited_from.present?
# }.map { |mr|
#   
#   mr.inherited_from_member_role.try(:member)
# }.compact.map
Query(MemberRole)
.where('role_id = ?')
.where('inherited_from != 0')
.select('member_id')
.where("id != 0")
# Q 476 : # members.includes(:user, :roles).inject({ })
Query(Member)
.includes('user')
.includes('roles')
# Q 477 : # members.preload(:principal).select { |m|
#   
#   m.principal.present? && (
#   m.mail_notification? || m.principal.mail_notification == "all")
# }.collect
Query(Member)
.joins('user')
.where('project_id = ?')
.where('user_id != 0')
.where('mail_notification = true')
.where("user.mail_notification = 'all'")
.includes('principal')
# Q 478 : # members.where(:project_id => ids).update_all(:mail_notification => true)
Query(Member)
.where("project_id = ?")
# Q 479 : # messages.where(:parent_id => nil)
Query(Message)
.where("parent_id = ?")
# Q 480: # projects.order('lft')
Query(Project)
.order('lft')
# Q 484 : # order(:name, :id)
# Q 485 : # order(:position)
Query(CustomField)
.order('position')
# Q 486 : # order(:position)
Query(Tracker)
.order('position')
# Q 487 : # order(:position)
Query(Enumeration)
.order('position')
# Q 488 : # order(:position)
Query(IssueStatus)
.order('position')
# Q 489 : # order(:position).where(:builtin => 0)
# Q 490 : # order(:type => :asc, :lastname => :asc)
Query(User)
.order('type, lastname')
# Q 491 : # order(:updated_on => :desc)
Query(Issue)
.order('updated_on')
# Q 492 : # order(fields_for_order_statement)
# Q 493 : # preload(:content_without_text)
Query(WikiPage)
.includes('content_without_text')
# Q 494 : # project.boards.visible.find_by_name(name)
Query(Board)
.joins('project')
.where("exists(project.enabled_modules, name = 'board')")
.where("project_id = ?")
.where("name = ?")
# Q 495 : # project.documents.visible.find_by_title(name)
Query(Document)
.where("project_id = ?")
.where("title = ?")
# Q 496 : # project.issue_categories.find_by_name(category.name)
Query(IssueCategory)
.where("project_id = ?")
.where("name = ?")
# Q 497 : # project.issues.reorder("root_id, lft").each
Query(Issue)
.where("project_id = ?")
.order('id, root_id, lft')
# Q 498 : # project.members.active.preload(:user)
Query(Member)
.joins('user')
.where("project_id = ?")
.where('user.status = 2')
.includes('user')
# Q 499 : # project.members.active.preload(:user)
Query(Member)
.where("project_id = ?")
.includes('user')
# Q 500 : # project.memberships.select
Query(Member)
.where("project_id = ?")
# Q 501 : # project.memberships.select
Query(Member)
.where("project_id = ?")
# Q 502 : # project.news.visible.find_by_title(name)
Query(News)
.where("project_id = ?")
.where("title = ?")
# Q 503 : # project.self_and_descendants.reload.pluck(:id)
Query(Project)
.select('id')
# Q 504 : # project.time_entry_activities.find_by_id(id.to_i)
Query(TimeEntryActivity)
.where("project_id = ?")
.where("id = ?")
# Q 505 : # project.trackers.first
Query(Tracker)
.where("id = ?")
.return_limit('1')
# Q 506 : # project.trackers.first.try(:id)
Query(Tracker)
.where("id = ?")
.return_limit('1')
.select('id')
# Q 507 : # project.users.preload(:preference).select(&:notify_about_high_priority_issues?)
# Q 508 : # project.versions.visible.find_by_name(name)
Query(Version)
.where("project_id = ?")
.where("name = ?")
# Q 509 : # project.wiki.find_page(title)
# Q 521 : # select(:id, :page_id, :version, :updated_on)
Query(WikiContent)
.select('id')
.select('page_id')
.select('version')
.select('updated_on')
# Q 522
Query(CustomFieldEnumeration)
.where("custom_field_id = ?")
# Q 525 : # self.class.where(issue_from_id: issue_to, issue_to_id: issue_from).present?
Query(IssueRelation)
.where("issue_from_id = ?")
.where("issue_to_id = ?")
# Q 526 : # self.class.where.not(:parent_id => nil).update_all("position = coalesce((
#           select position
#           from (select id, position from enumerations) as parent
#           where parent_id = parent.id), 1)")
Query(Enumeration)
.where("parent_id != 0")
# Q 527 : # self.find(*args)
Query(Project)
.where("id = ?")
# Q 528 : # self.time_entries.where(:activity_id => parent_activity.id).update_all(:activity_id => project_activity.id)
Query(TimeEntry)
.where("project_id = ?")
.where("activity_id = ?")
# Q 529 : # self.time_entry_activities.pluck(:parent_id).compact
Query(TimeEntryActivity)
.where("project_id = ?")
.select('parent_id')
.where("id != 0")
# Q 530 : # self.wiki.find_page(t)
Query(Wiki)
.where("id = ?")
# Q 534 : # user.groups.any?
Query(Group)
.where('user_id = ?')
.where("id = ?")
# Q 535 : # user.groups.include?(principal)
Query(Group)
.where("id = ?")
# Q 536 : # user.groups.pluck(:id).compact
Query(Group)
.where('user_id = ?')
.select('id')
.where("id != 0")
# Q 537 : # user.groups.pluck(:id).compact
Query(Group)
.where("id = ?")
.select('id')
.where("id != 0")
# Q 538 : # user.lastname.blank?
Query(User)
.select('lastname')
# Q 539 : # user.memberships.joins(:member_roles).where(:member_roles => { :role_id => roles.map(&:id) }).any?
Query(Member)
.where("user_id = ?")
.joins('member_roles')
.where("member_roles.role_id = ?")
# Q 540 : # user.projects.active.select(:id, :name, :identifier, :lft, :rgt).to_a
Query(Project)
.joins('members')
.where("members.user_id = ?")
.select('id')
.select('name')
.select('identifier')
.select('lft')
.select('rgt')
# Q 541 : # user_custom_fields.pluck(:name)
Query(UserCustomField)
.select('name')
# Q 546 : # versions.where(:status => %w{open locked}).each
Query(Version)
.where("status = 'open'")
.pred_or("status = 'locked'")
# Q 547 : # watchers.where(:user_id => user.id).delete_all
Query(Watcher)
.where("user_id IN (?, ?)")
# Q 548 : # where("Project.id IN (SELECT em.project_id FROM EnabledModule em WHERE em.name=?)", mod.to_s)
Query(Project)
.where('exists(enabled_modules, name = ?)')
# Q 549 : # where("LOWER(#{
# table_name}.name) = LOWER(?)", arg.to_s.strip)
Query(Enumeration)
.where('name = ?')
# Q 550 : # where("LOWER(#{
# table_name}.name) = LOWER(?)", arg.to_s.strip)
Query(Version)
.where('name = ?')
# Q 551 : # where("LOWER(#{
# table_name}.name) = LOWER(?)", arg.to_s.strip)
Query(IssueCategory)
.where('name = ?')
# Q 552 : # where("LOWER(#{
# table_name}.name) = LOWER(?)", arg.to_s.strip)
Query(Tracker)
.where('name = ?')
# Q 553 : # where("LOWER(#{
# table_name}.name) = LOWER(?)", arg.to_s.strip)
Query(IssueStatus)
.where('name = ?')
# Q 554 : # where(:active => true)
Query(Enumeration)
.where("active = ?")
# Q 555 : # where(:active => true)
Query(CustomFieldEnumeration)
.where("active = ?")
# Q 556 : # where(:admin => admin)
Query(User)
.where("admin = ?")
# Q 557 : # where(:identity_url => url).first
Query(User)
.where("identity_url = ?")
.return_limit('1')
# Q 558 : # where(:is_default => true).first
Query(Enumeration)
.where("is_default = ?")
.return_limit('1')
# Q 559 : # where(:is_default => true, :type => "Enumeration").first
Query(Enumeration)
.where("is_default = true")
.where("type = 'Enumeration'")
.return_limit('1')
# Q 560 : # where(:is_public => true)
Query(Project)
.where("is_public = true")
# Q 561 : # where(:name => name).order(:id => :desc).first
Query(Setting)
.where("name = ?")
.order('id')
.return_limit('1')
# Q 562 : # where(:project_id => (
# project.nil? ? nil : [nil, project.id]))
# Q 563 : # where(:project_id => nil)
Query(Enumeration)
.where("project_id = ?")
# Q 564 : # where(:project_id => nil)
Query(Enumeration)
.where("project_id = 0")
# Q 565 : # where(:status => "open")
Query(Version)
.where("status = 'open'")
# Q 566 : # where(:status => STATUS_ACTIVE)
Query(Project)
.where("status = 1")
# Q 567 : # where(:status => STATUS_ACTIVE)
Query(Principal)
.where("status = 1")
# Q 568 : # where(:type => "Group")
Query(Group)
.where("type = 'Group'")
# Q 569 : # wiki.find_page(redirects_to, :with_redirect => false)
Query(Wiki)

