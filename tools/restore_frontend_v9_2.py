from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
original = s

def replace_once(old, new, label):
    global s
    n = s.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 match, found {n}')
    s = s.replace(old, new, 1)

replace_once(
    '<div style="margin-bottom:8px; width:36px; height:36px; border-radius:50%; background:#FFF; color:var(--primary); display:flex; align-items:center; justify-content:center; font-weight:900; font-size:16px;">UAF</div>',
    '<div style="margin-bottom:8px; width:36px; height:36px; border-radius:50%; background:#FFF; display:flex; align-items:center; justify-content:center; overflow:hidden;"><img src="./icon-192.png" alt="UAF" style="width:100%; height:100%; object-fit:cover; border-radius:50%;"></div>',
    'sidebar logo')

replace_once(
    "${canManage ? `<button class=\"btn secondary\" style=\"padding:3px 8px; font-size:11px;\" onclick=\"startWhatsAppChatWithContact('${c.email}', '${escapeHtml(c.name)}')\">Chat</button>` : '—'}",
    "${canManage ? `<button class=\"btn secondary\" style=\"padding:3px 8px; font-size:11px;\" onclick=\"startWhatsAppChatWithContact('${c.email}', '${escapeHtml(c.name)}')\">Chat</button>` : '—'} ${currentUser && currentUser.isSuperAdmin ? `<button class=\"btn secondary\" style=\"padding:3px 8px; font-size:11px; margin-left:4px;\" onclick=\"openEditContactModal('${c.id}')\">Edit</button>` : ''}",
    'contact edit action')

replace_once(
    '<div style="display:flex; gap:8px; align-items:center;" id="fin-actions-bar"></div>',
    '<div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;" id="fin-actions-bar"><button class="btn" id="fin-add-income-btn" onclick="openAddIncomeModal()">+ Income</button><button class="btn" id="fin-add-expense-btn" onclick="openAddExpenseModal()">+ Expense</button><button class="btn secondary" id="fin-update-org-btn" onclick="openModal(\'modal-update-org\')">Adjust Balance</button><button class="btn secondary" id="fin-add-initiative-btn" onclick="openAddInitiativeModal()">+ Initiative</button><button class="btn secondary" id="fin-report-btn" onclick="openFinancialReportModal()">📊 Financial Report</button></div>',
    'finance action bar')

replace_once(
    '<button class="wa-icon-btn" onclick="loadChats()" title="Refresh">🔄</button>',
    '<button class="wa-icon-btn" onclick="openNewChatPicker()" title="New Chat">➕</button><button class="wa-icon-btn" onclick="openNewGroupModal()" title="New Group">👥</button><button class="wa-icon-btn" onclick="loadChats()" title="Refresh">🔄</button>',
    'chat list actions')

replace_once(
    '</div>\n              <div class="wa-room-messages" id="wa-messages-feed"></div>',
    '</div>\n              <div style="display:flex; align-items:center; gap:6px; padding:6px 10px; background:var(--wa-teal-dark); border-top:1px solid rgba(255,255,255,.08);">\n                <button class="wa-icon-btn" id="wa-audio-call-btn" onclick="startAudioCall()" title="Start Audio Call">📞</button>\n                <span id="wa-call-status" style="font-size:11px; color:rgba(255,255,255,.9);">Audio calls only</span>\n              </div>\n              <div id="wa-active-call-banner" style="display:none; padding:8px 12px; background:#ECFDF5; border-bottom:1px solid #A7F3D0; color:#065F46; font-size:12px; font-weight:700;"></div>\n              <div class="wa-room-messages" id="wa-messages-feed"></div>',
    'chat room controls')

modal_anchor = '  <!-- CHANGE PASSWORD MODAL -->'
if s.count(modal_anchor) != 1: raise SystemExit('modal anchor mismatch')
modals = '''
  <!-- RESTORED: EDIT CONTACT MODAL -->
  <div class="modal" id="modal-edit-contact">
    <div class="modal-card">
      <input type="hidden" id="edit-con-id">
      <h3 style="margin:0 0 14px; font-size:17px; font-weight:800; color:var(--navy-text);">Edit Organization Contact</h3>
      <div class="field"><label>Contact Name *</label><input type="text" id="edit-con-name" required></div>
      <div class="field"><label>Institution / Organization</label><input type="text" id="edit-con-institution"></div>
      <div class="field"><label>Category</label><select id="edit-con-category"><option value="Government">Government Agency</option><option value="International Partner">International Partner</option><option value="Local NGO">Local NGO</option><option value="Community Leader">Community Leader</option><option value="Youth Leader">Youth Leader</option><option value="Media">Media / Press</option><option value="Other">Other</option></select></div>
      <div class="field"><label>Email Address</label><input type="email" id="edit-con-email"></div>
      <div class="field"><label>Phone / WhatsApp</label><input type="tel" id="edit-con-phone"></div>
      <div class="field"><label>Physical Address</label><input type="text" id="edit-con-address"></div>
      <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:16px;"><button class="btn secondary" onclick="closeModal('modal-edit-contact')">Cancel</button><button class="btn" onclick="submitEditContact()">Update Contact</button></div>
    </div>
  </div>

  <!-- RESTORED: ADD INITIATIVE MODAL -->
  <div class="modal" id="modal-add-initiative">
    <div class="modal-card">
      <h3 style="margin:0 0 14px; font-size:17px; font-weight:800; color:var(--navy-text);">Create Finance Initiative</h3>
      <div class="field"><label>Initiative Name *</label><input type="text" id="initiative-name" required></div>
      <div style="display:grid; grid-template-columns:1fr 110px; gap:10px;"><div class="field"><label>Starting Amount</label><input type="number" step="any" id="initiative-amount" value="0"></div><div class="field"><label>Currency</label><select id="initiative-currency"><option value="USD">USD ($)</option><option value="LRD">LRD (L$)</option></select></div></div>
      <div class="field"><label>Status</label><select id="initiative-status"><option value="Active">Active</option><option value="Planned">Planned</option><option value="Closed">Closed</option></select></div>
      <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:16px;"><button class="btn secondary" onclick="closeModal('modal-add-initiative')">Cancel</button><button class="btn" onclick="submitNewInitiative()">Create Initiative</button></div>
    </div>
  </div>

  <!-- RESTORED: ORG-WIDE FINANCIAL REPORT MODAL -->
  <div class="modal" id="modal-financial-report">
    <div class="modal-card" style="max-width:760px;">
      <h3 style="margin:0 0 8px; font-size:17px; font-weight:800; color:var(--navy-text);">📊 Organization-wide Financial Report</h3>
      <p style="font-size:12.5px; color:var(--muted); margin:0 0 14px;">Filter the FinanceLedger by date and export the resulting rows as CSV.</p>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;"><div class="field"><label>Start Date</label><input type="date" id="fin-report-start"></div><div class="field"><label>End Date</label><input type="date" id="fin-report-end"></div></div>
      <div id="fin-report-result" style="max-height:360px; overflow:auto; margin-top:8px;"></div>
      <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:16px;"><button class="btn secondary" onclick="closeModal('modal-financial-report')">Close</button><button class="btn" onclick="generateFinancialReportUI()">Generate &amp; Download CSV</button></div>
    </div>
  </div>

  <!-- RESTORED: NEW GROUP MODAL -->
  <div class="modal" id="modal-new-group">
    <div class="modal-card" style="max-width:620px;">
      <h3 style="margin:0 0 14px; font-size:17px; font-weight:800; color:var(--navy-text);">Create New Group Chat</h3>
      <div class="field"><label>Group Name *</label><input type="text" id="new-group-name" placeholder="e.g. Programs Team"></div>
      <div class="field"><label>Select Team Members</label><input type="text" id="group-member-search" placeholder="Search members..." oninput="renderGroupMemberPicker(this.value)"></div>
      <div id="group-member-list" style="max-height:280px; overflow:auto; border:1px solid var(--line); border-radius:var(--radius-md); padding:6px;"></div>
      <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:16px;"><button class="btn secondary" onclick="closeModal('modal-new-group')">Cancel</button><button class="btn" onclick="submitNewGroup()">Create Group</button></div>
    </div>
  </div>

  <!-- RESTORED: NEW CHAT PICKER -->
  <div class="modal" id="modal-new-chat">
    <div class="modal-card" style="max-width:620px;">
      <h3 style="margin:0 0 12px; font-size:17px; font-weight:800; color:var(--navy-text);">Start New Chat</h3>
      <div class="field"><input type="text" id="new-chat-search" placeholder="Search team members and contacts..." oninput="renderNewChatPicker(this.value)"></div>
      <div id="new-chat-list" style="max-height:360px; overflow:auto; border:1px solid var(--line); border-radius:var(--radius-md); padding:6px;"></div>
      <div style="display:flex; justify-content:flex-end; margin-top:14px;"><button class="btn secondary" onclick="closeModal('modal-new-chat')">Close</button></div>
    </div>
  </div>

  <!-- RESTORED: AUDIO CALL MODAL (NO CAMERA / NO VIDEO) -->
  <div class="modal" id="modal-audio-call">
    <div class="modal-card" style="max-width:420px; text-align:center;">
      <div style="font-size:42px; margin-bottom:8px;">📞</div>
      <h3 style="margin:0 0 6px; font-size:18px; font-weight:800; color:var(--navy-text);">UAF Audio Call</h3>
      <div id="audio-call-peer" style="font-size:13px; color:var(--muted); margin-bottom:16px;">Audio-only call</div>
      <div style="display:flex; justify-content:center; gap:10px;"><button class="btn" id="audio-call-mute" onclick="toggleAudioCallMute()">🔇 Mute</button><button class="btn danger" onclick="endAudioCall()">End Call</button></div>
      <div id="audio-call-note" style="font-size:11.5px; color:var(--muted); margin-top:14px;">Microphone permission is requested only when you start an audio call.</div>
    </div>
  </div>

'''
s = s.replace(modal_anchor, modals + modal_anchor, 1)

js_anchor = '// Settings Theme & Auth'
if s.count(js_anchor) != 1: raise SystemExit('JS anchor mismatch')
js = '''
// ==================== RESTORED v9.2 FEATURES ====================
function openEditContactModal(contactId) {
  const c = (allContacts || []).find(x => x.id === contactId);
  if (!c || !(currentUser && currentUser.isSuperAdmin)) return;
  document.getElementById('edit-con-id').value = c.id;
  document.getElementById('edit-con-name').value = c.name || '';
  document.getElementById('edit-con-institution').value = c.institution || '';
  document.getElementById('edit-con-category').value = c.category || 'Other';
  document.getElementById('edit-con-email').value = c.email || '';
  document.getElementById('edit-con-phone').value = c.phone || '';
  document.getElementById('edit-con-address').value = c.address || '';
  openModal('modal-edit-contact');
}
async function submitEditContact() {
  if (!(currentUser && currentUser.isSuperAdmin)) return;
  const contactId = document.getElementById('edit-con-id').value;
  const name = document.getElementById('edit-con-name').value.trim();
  if (!name) { alert('Contact name is required.'); return; }
  const res = await apiPost('updateContact', { contactId, name, category: document.getElementById('edit-con-category').value, phone: document.getElementById('edit-con-phone').value.trim(), contactEmail: document.getElementById('edit-con-email').value.trim(), institution: document.getElementById('edit-con-institution').value.trim(), address: document.getElementById('edit-con-address').value.trim() });
  if (res.error) { alert(res.error); return; }
  closeModal('modal-edit-contact'); await loadContacts();
}
function openAddInitiativeModal() {
  if (!(currentUser && currentUser.isSuperAdmin)) return;
  document.getElementById('initiative-name').value = '';
  document.getElementById('initiative-amount').value = '0';
  document.getElementById('initiative-currency').value = 'USD';
  document.getElementById('initiative-status').value = 'Active';
  openModal('modal-add-initiative');
}
async function submitNewInitiative() {
  if (!(currentUser && currentUser.isSuperAdmin)) return;
  const name = document.getElementById('initiative-name').value.trim();
  if (!name) { alert('Initiative name is required.'); return; }
  const res = await apiPost('addInitiative', { name, amountReceived: document.getElementById('initiative-amount').value, currency: document.getElementById('initiative-currency').value, status: document.getElementById('initiative-status').value });
  if (res.error) { alert(res.error); return; }
  closeModal('modal-add-initiative'); await loadFinances(); switchFinSubTab('initiatives');
}
function openFinancialReportModal() {
  if (!(currentUser && currentUser.isSuperAdmin)) return;
  document.getElementById('fin-report-start').value = '';
  document.getElementById('fin-report-end').value = '';
  document.getElementById('fin-report-result').innerHTML = '';
  openModal('modal-financial-report');
}
function csvEscape(v) { const s = v == null ? '' : String(v); return /[",\\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; }
async function generateFinancialReportUI() {
  if (!(currentUser && currentUser.isSuperAdmin)) return;
  const startDate = document.getElementById('fin-report-start').value;
  const endDate = document.getElementById('fin-report-end').value;
  const result = document.getElementById('fin-report-result');
  result.innerHTML = '<div style="padding:12px; color:var(--muted);">Generating report…</div>';
  const res = await apiPost('generateFinancialReport', { startDate, endDate });
  if (res.error) { result.innerHTML = `<div style="padding:12px; color:var(--danger);">${escapeHtml(res.error)}</div>`; return; }
  const rows = Array.isArray(res.rows) ? res.rows : [];
  const headers = ['ID','Date','User','Type','Category','Amount','Currency','Description'];
  const csv = [headers.join(','), ...rows.map(r => [r.id,r.date,r.user,r.type,r.category,r.amount,r.currency,r.description].map(csvEscape).join(','))].join('\\n');
  const blob = new Blob([csv], {type:'text/csv;charset=utf-8;'});
  const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = `UAF_Financial_Report_${startDate || 'all'}_${endDate || 'all'}.csv`; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  result.innerHTML = `<div style="padding:12px;">Generated <strong>${rows.length}</strong> ledger row(s). The CSV download has started.</div>`;
}
let selectedGroupMembers = new Set();
function openNewGroupModal() { selectedGroupMembers = new Set(); document.getElementById('new-group-name').value = ''; document.getElementById('group-member-search').value = ''; renderGroupMemberPicker(''); openModal('modal-new-group'); }
function renderGroupMemberPicker(q) {
  q = (q || '').toLowerCase().trim();
  const list = (allTeamProfiles || []).filter(p => p.email && p.email.toLowerCase() !== (currentUser?.email || '').toLowerCase()).filter(p => `${p.displayName || p.name} ${p.email} ${p.currentPosition || ''}`.toLowerCase().includes(q));
  document.getElementById('group-member-list').innerHTML = list.map(p => { const checked = selectedGroupMembers.has(p.email.toLowerCase()); return `<label style="display:flex; align-items:center; gap:9px; padding:8px; border-bottom:1px solid var(--line); cursor:pointer;"><input type="checkbox" ${checked ? 'checked' : ''} onchange="toggleGroupMember('${escapeHtml(p.email)}', this.checked)">${getAvatarHtml(p.email, p.displayName || p.name, p.photoUrl, 30)}<span><strong>${escapeHtml(p.displayName || p.name)}</strong><br><span style="font-size:11px; color:var(--muted);">${escapeHtml(p.currentPosition || p.email)}</span></span></label>`; }).join('') || '<div style="padding:12px; color:var(--muted);">No matching team members.</div>';
}
function toggleGroupMember(email, checked) { const key = email.toLowerCase(); if (checked) selectedGroupMembers.add(key); else selectedGroupMembers.delete(key); }
async function submitNewGroup() {
  const groupName = document.getElementById('new-group-name').value.trim(); const memberEmails = Array.from(selectedGroupMembers);
  if (!groupName) { alert('Group name is required.'); return; } if (!memberEmails.length) { alert('Select at least one member.'); return; }
  const res = await apiPost('createGroup', { groupName, memberEmails }); if (res.error) { alert(res.error); return; }
  closeModal('modal-new-group'); await loadChats(); const members = allTeamProfiles.filter(p => memberEmails.includes(p.email.toLowerCase())); openWhatsAppChatRoom(res.channelId, groupName, members[0]?.photoUrl || '', false);
}
function openNewChatPicker() { document.getElementById('new-chat-search').value = ''; renderNewChatPicker(''); openModal('modal-new-chat'); }
function renderNewChatPicker(q) {
  q = (q || '').toLowerCase().trim();
  const team = (allTeamProfiles || []).filter(p => p.email && p.email.toLowerCase() !== (currentUser?.email || '').toLowerCase()).filter(p => `${p.displayName || p.name} ${p.email} ${p.currentPosition || ''}`.toLowerCase().includes(q));
  const contacts = (allContacts || []).filter(c => c.email).filter(c => `${c.name} ${c.institution || ''} ${c.email}`.toLowerCase().includes(q));
  const teamHtml = team.map(p => `<button class="btn secondary" style="width:100%; justify-content:flex-start; margin-bottom:6px;" onclick="startNewDM('${escapeHtml(p.email)}','${escapeHtml(p.displayName || p.name)}')">${getAvatarHtml(p.email,p.displayName||p.name,p.photoUrl,30)}<span>${escapeHtml(p.displayName || p.name)} <small style="color:var(--muted);">• Team</small></span></button>`).join('');
  const contactHtml = contacts.map(c => `<button class="btn secondary" style="width:100%; justify-content:flex-start; margin-bottom:6px;" onclick="startNewDM('${escapeHtml(c.email)}','${escapeHtml(c.name)}')">👤 <span>${escapeHtml(c.name)} <small style="color:var(--muted);">• ${escapeHtml(c.institution || c.category || 'Contact')}</small></span></button>`).join('');
  document.getElementById('new-chat-list').innerHTML = teamHtml + contactHtml || '<div style="padding:12px; color:var(--muted);">No matching people or contacts.</div>';
}
async function startNewDM(email, name) { const res = await apiPost('getOrCreateDM', { emailB: email }); if (res.error) { alert(res.error); return; } closeModal('modal-new-chat'); await loadChats(); openWhatsAppChatRoom(res.channelId, name, '', false); }
let voiceRecorder = null, voiceChunks = [], voiceRecording = false;
async function startVoiceRecording() {
  if (!navigator.mediaDevices?.getUserMedia || typeof MediaRecorder === 'undefined') { alert('Voice recording is not supported by this browser.'); return; }
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true }); voiceChunks = []; voiceRecorder = new MediaRecorder(stream);
    voiceRecorder.ondataavailable = e => { if (e.data && e.data.size) voiceChunks.push(e.data); };
    voiceRecorder.onstop = async () => {
      stream.getTracks().forEach(t => t.stop()); const blob = new Blob(voiceChunks, {type: voiceRecorder.mimeType || 'audio/webm'}); voiceRecorder = null; voiceRecording = false;
      const btn = document.getElementById('wa-mic-send-btn'); if (btn) btn.innerText = '🎙️'; if (!blob.size) return;
      const fileName = `voice-${Date.now()}.webm`; const file = new File([blob], fileName, {type: blob.type}); const base64 = await fileToBase64(file);
      const up = await apiPost('uploadFile', {base64Data:base64, fileName, mimeType:blob.type}); if (!up.directUrl) { alert(up.error || 'Voice upload failed.'); return; }
      const res = await apiPost('postMessage', {channelId:activeChannelId, name:currentUser.displayName || currentUser.name, text:'', type:'voice', link:up.directUrl}); if (res.error) alert(res.error); else loadWhatsAppMessages();
    };
    voiceRecorder.start(); voiceRecording = true; const btn = document.getElementById('wa-mic-send-btn'); if (btn) btn.innerText = '⏹️';
  } catch (e) { alert('Microphone permission was not granted.'); }
}
function stopVoiceRecording() { if (voiceRecorder && voiceRecording) voiceRecorder.stop(); }
function handleWhatsAppActionButtonRestored() { const input = document.getElementById('wa-message-input'); if (input.value.trim()) sendWhatsAppMessage(); else if (voiceRecording) stopVoiceRecording(); else startVoiceRecording(); }
let audioCallPeerConnection = null, audioCallStream = null, audioCallMuted = false, activeCallPoll = null;
async function startAudioCall() {
  if (!currentUser || !activeChannelId) return;
  try {
    if (!navigator.mediaDevices?.getUserMedia || !window.RTCPeerConnection) { alert('Audio calling is not supported by this browser.'); return; }
    audioCallStream = await navigator.mediaDevices.getUserMedia({audio:true});
    audioCallPeerConnection = new RTCPeerConnection({iceServers:[{urls:'stun:stun.l.google.com:19302'}]});
    audioCallStream.getTracks().forEach(track => audioCallPeerConnection.addTrack(track, audioCallStream));
    audioCallPeerConnection.ontrack = event => { let audio = document.getElementById('uaf-remote-audio'); if (!audio) { audio = document.createElement('audio'); audio.id='uaf-remote-audio'; audio.autoplay=true; audio.controls=false; audio.style.display='none'; document.body.appendChild(audio); } audio.srcObject=event.streams[0]; };
    const res = await apiPost('notifyCall', {name:currentUser.displayName || currentUser.name, channelId:activeChannelId, channelName:currentActiveChannel?.title || 'Team Chat'}); if (res.error) { alert(res.error); endAudioCall(); return; }
    document.getElementById('audio-call-peer').innerText = currentActiveChannel?.title || 'Team Chat'; document.getElementById('audio-call-note').innerText = 'Audio-only call session active. No camera or video is used.'; openModal('modal-audio-call'); startActiveCallPolling();
  } catch(e) { alert('Unable to start audio call: ' + (e.message || 'microphone unavailable')); endAudioCall(); }
}
function toggleAudioCallMute() { audioCallMuted=!audioCallMuted; if(audioCallStream) audioCallStream.getAudioTracks().forEach(t=>t.enabled=!audioCallMuted); const b=document.getElementById('audio-call-mute'); if(b) b.innerText=audioCallMuted?'🔊 Unmute':'🔇 Mute'; }
function endAudioCall() { if(audioCallPeerConnection){try{audioCallPeerConnection.close();}catch(e){}} audioCallPeerConnection=null; if(audioCallStream) audioCallStream.getTracks().forEach(t=>t.stop()); audioCallStream=null; audioCallMuted=false; const audio=document.getElementById('uaf-remote-audio'); if(audio){audio.srcObject=null;audio.remove();} if(activeCallPoll){clearInterval(activeCallPoll);activeCallPoll=null;} closeModal('modal-audio-call'); }
async function checkActiveAudioCall() { const res=await apiFetchAction('activeCall'); const banner=document.getElementById('wa-active-call-banner'); if(!banner)return; if(res&&res.isLive){banner.innerHTML=`📞 <strong>${escapeHtml(res.startedBy||'A team member')}</strong> started a live audio call. <button class="btn" style="padding:3px 8px; font-size:11px; margin-left:8px;" onclick="startAudioCall()">Join Audio Call</button>`;banner.style.display='block';}else banner.style.display='none'; }
function startActiveCallPolling(){if(activeCallPoll)clearInterval(activeCallPoll);checkActiveAudioCall();activeCallPoll=setInterval(checkActiveAudioCall,10000);}
window.handleWhatsAppActionButton = handleWhatsAppActionButtonRestored;
const _uafOriginalLoadWhatsAppMessages = loadWhatsAppMessages;
loadWhatsAppMessages = async function(){ if(!activeChannelId)return; const msgs=await cachedFetch(`messages&channelId=${activeChannelId}`,`msgs_${activeChannelId}`); const feed=document.getElementById('wa-messages-feed'); if(!Array.isArray(msgs))return; feed.innerHTML=msgs.map(m=>{const isMine=currentUser&&m.email.toLowerCase()===currentUser.email.toLowerCase(); const body=m.type==='voice'&&m.link?`<div style="display:flex;align-items:center;gap:8px;"><span>🎤</span><audio controls preload="metadata" src="${escapeHtml(m.link)}" style="max-width:210px;height:34px;"></audio></div>`:`<div>${formatMentionsAndText(m.text||'')}</div>`; return `<div class="wa-msg-bubble ${isMine?'wa-msg-mine':'wa-msg-other'}">${!isMine?`<div class="wa-msg-author">${escapeHtml(m.name)}</div>`:''}${body}<div class="wa-msg-meta"><span>${new Date(m.timestamp).toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'})}</span>${isMine?'<span style="color:#53BDEB;">✓✓</span>':''}</div></div>`;}).join('');feed.scrollTop=feed.scrollHeight; };
const _uafOriginalSwitchTab = switchTab;
switchTab = function(tabName){ _uafOriginalSwitchTab(tabName); if(tabName==='chats') startActiveCallPolling(); else if(activeCallPoll){clearInterval(activeCallPoll);activeCallPoll=null;} };

'''
s = s.replace(js_anchor, js + js_anchor, 1)

if s == original: raise SystemExit('Patch produced no changes')
p.write_text(s, encoding='utf-8')
print(f'patched {len(original)} -> {len(s)}')
