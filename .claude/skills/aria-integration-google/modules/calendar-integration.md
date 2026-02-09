# Google Calendar Integration Module

## Overview

Google Calendar API integration for regulatory schedule management in ARIA Phase 4.

## MCP Tool Interfaces

### 1. Create Event

```typescript
interface CalendarEventParams {
  title: string;
  description?: string;
  start: Date;
  end: Date;
  attendees?: string[];
  location?: string;
  recurrence?: string;
}

interface CalendarEventResponse {
  eventId: string;
  htmlLink: string;
}
```

**Tool**: `mcp__google-workspace__calendar_create`

### 2. Query Events

```typescript
interface CalendarQueryParams {
  timeMin: Date;
  timeMax: Date;
  q?: string; // search query
}

interface CalendarEvent {
  id: string;
  summary: string;
  start: { dateTime?: string; date?: string };
  end: { dateTime?: string; date?: string };
  description?: string;
  attendees?: Array<{ email: string; responseStatus: string }>;
}
```

**Tool**: `mcp__google-workspace__calendar_query`

## Regulatory Calendar Templates

### 1. Regulatory Review Schedule

```typescript
interface RegulatoryReviewEvent {
  submissionId: string;
  reviewType: 'Internal' | 'External' | 'FDA' | 'Notified Body' | 'MFDS';
  title: string;
  description: string;
  location: string;
  duration: number; // minutes
  attendees: string[];
  reminderDays: number;
}

async function createRegulatoryReviewEvent(
  event: RegulatoryReviewEvent
): Promise<string> {
  const startTime = new Date();
  const endTime = new Date(startTime.getTime() + event.duration * 60 * 1000);

  // Add reminders
  const reminders = event.attendees.map(email => ({
    email,
    reminders: {
      useDefault: false,
      overrides: [
        { method: 'email', minutes: event.reminderDays * 24 * 60 },
        { method: 'popup', minutes: 60 }
      ]
    }
  }));

  const result = await mcp__google-workspace__calendar_create({
    title: `[${event.reviewType}] ${event.title}`,
    description: `
${event.description}

Submission ID: ${event.submissionId}
Review Type: ${event.reviewType}

ARIA Regulatory Manager
    `.trim(),
    start: startTime,
    end: endTime,
    location: event.location,
    attendees: event.attendees
  });

  return result.eventId;
}
```

### 2. Audit Schedule

```typescript
interface AuditScheduleEvent {
  auditId: string;
  auditType: 'Internal' | 'External' | 'Supplier';
  title: string;
  description: string;
  location: string;
  duration: number;
  attendees: string[];
  checklistRequired: boolean;
}

async function createAuditSchedule(
  event: AuditScheduleEvent
): Promise<string> {
  const startTime = new Date();
  const endTime = new Date(startTime.getTime() + event.duration * 60 * 1000);

  const description = `
${event.description}

Audit ID: ${event.auditId}
Audit Type: ${event.auditType}

${event.checklistRequired ? 'Checklist Required: Yes' : ''}

ARIA Regulatory Manager
  `.trim();

  const result = await mcp__google-workspace__calendar_create({
    title: `[${event.auditType} Audit] ${event.title}`,
    description,
    start: startTime,
    end: endTime,
    location: event.location,
    attendees: event.attendees
  });

  return result.eventId;
}
```

### 3. Recurring Compliance Tasks

```typescript
interface RecurringComplianceTask {
  taskId: string;
  title: string;
  description: string;
  frequency: 'DAILY' | 'WEEKLY' | 'MONTHLY' | 'QUARTERLY' | 'YEARLY';
  interval: number;
  duration: number;
  attendees: string[];
  until?: Date;
}

async function createRecurringComplianceTask(
  task: RecurringComplianceTask
): Promise<string> {
  const startTime = new Date();
  startTime.setHours(10, 0, 0, 0); // 10 AM
  const endTime = new Date(startTime.getTime() + task.duration * 60 * 1000);

  // Build recurrence rule
  const recurrenceRule = `RRULE:FREQ=${task.frequency};INTERVAL=${task.interval}`;

  const result = await mcp__google-workspace__calendar_create({
    title: `[Compliance] ${task.title}`,
    description: `
${task.description}

Task ID: ${task.taskId}
Frequency: ${task.frequency}

ARIA Regulatory Manager
    `.trim(),
    start: startTime,
    end: endTime,
    attendees: task.attendees,
    recurrence: recurrenceRule
  });

  return result.eventId;
}

// Example: Quarterly Internal Audit
await createRecurringComplianceTask({
  taskId: 'QUARTERLY-AUDIT-001',
  title: 'Quarterly Internal Audit',
  description: 'Quarterly ISO 13485 internal audit per clause 8.2.2',
  frequency: 'MONTHLY',
  interval: 3, // Every 3 months
  duration: 120, // 2 hours
  attendees: ['quality@company.com', 'regulatory@company.com']
});

// Example: Weekly CAPA Review
await createRecurringComplianceTask({
  taskId: 'WEEKLY-CAPA-001',
  title: 'Weekly CAPA Status Review',
  description: 'Review open CAPAs and effectiveness checks',
  frequency: 'WEEKLY',
  interval: 1, // Every week
  duration: 60, // 1 hour
  attendees: ['quality@company.com', 'production@company.com']
});
```

### 4. Submission Deadline Reminder

```typescript
interface SubmissionDeadlineReminder {
  submissionId: string;
  submissionType: '510(k)' | 'PMA' | 'CE' | 'MFDS';
  targetMarket: string;
  deadline: Date;
  attendees: string[];
}

async function createDeadlineReminder(
  reminder: SubmissionDeadlineReminder
): Promise<string> {
  const deadline = reminder.deadline;

  // Create reminder 30 days before deadline
  const reminderDate = new Date(deadline);
  reminderDate.setDate(reminderDate.getDate() - 30);

  const result = await mcp__google-workspace__calendar_create({
    title: `[Reminder] ${reminder.submissionType} Deadline Approaching`,
    description: `
Submission ID: ${reminder.submissionId}
Submission Type: ${reminder.submissionType}
Target Market: ${reminder.targetMarket}
Deadline: ${deadline.toISOString()}

Days Remaining: 30

ARIA Regulatory Manager
    `.trim(),
    start: reminderDate,
    end: new Date(reminderDate.getTime() + 60 * 60 * 1000), // 1 hour meeting
    attendees: reminder.attendees
  });

  return result.eventId;
}
```

## Event Query and Filtering

### Query Regulatory Events

```typescript
async function getRegulatoryEvents(
  timeMin: Date,
  timeMax: Date
): Promise<CalendarEvent[]> {
  const events = await mcp__google-workspace__calendar_query({
    timeMin,
    timeMax,
    q: 'regulatory audit compliance submission CAPA'
  });

  return events.filter(event =>
    event.summary.includes('[FDA]') ||
    event.summary.includes('[Audit]') ||
    event.summary.includes('[Compliance]') ||
    event.summary.includes('[Internal]') ||
    event.summary.includes('[External]')
  );
}
```

### Get Upcoming Deadlines

```typescript
async function getUpcomingDeadlines(
  daysAhead: number = 30
): Promise<CalendarEvent[]> {
  const now = new Date();
  const future = new Date(now.getTime() + daysAhead * 24 * 60 * 60 * 1000);

  const events = await mcp__google-workspace__calendar_query({
    timeMin: now,
    timeMax: future,
    q: 'deadline due reminder'
  });

  return events.sort((a, b) => {
    const aStart = new Date(a.start.dateTime || a.start.date);
    const bStart = new Date(b.start.dateTime || b.start.date);
    return aStart.getTime() - bStart.getTime();
  });
}
```

## Integration with Notion

### Sync Calendar Events to Notion

```typescript
async function syncEventsToNotion(
  notionDatabaseId: string
): Promise<void> {
  const now = new Date();
  const future = new Date(now.getTime() + 90 * 24 * 60 * 60 * 1000); // Next 90 days

  const events = await mcp__google-workspace__calendar_query({
    timeMin: now,
    timeMax: future
  });

  for (const event of events) {
    const startTime = event.start.dateTime || event.start.date;
    const endTime = event.end.dateTime || event.end.date;

    await mcp__notion__create-page({
      databaseId: notionDatabaseId,
      properties: {
        'Event ID': { title: [{ text: { content: event.id } }] },
        'Event Name': { rich_text: [{ text: { content: event.summary } }] },
        'Start Date': { date: { start: startTime } },
        'End Date': { date: { start: endTime } },
        'Location': { rich_text: [{ text: { content: event.location || '' } }] },
        'Status': { status: { name: 'Scheduled' } }
      }
    });
  }
}
```

## Calendar Colors and Visibility

### Color Coding Scheme

```typescript
interface CalendarColorScheme {
  [key: string]: {
    colorId: string;
    description: string;
  };
}

const regulatoryColors: CalendarColorScheme = {
  'FDA': {
    colorId: '1', // Blue
    description: 'FDA-related events'
  },
  'Audit': {
    colorId: '2', // Green
    description: 'Audit events'
  },
  'CAPA': {
    colorId: '3', // Purple
    description: 'CAPA-related events'
  },
  'Compliance': {
    colorId: '4', // Red
    description: 'Compliance tasks'
  },
  'Submission': {
    colorId: '5', // Yellow
    description: 'Submission deadlines'
  },
  'Training': {
    colorId: '6', // Orange
    description: 'Training events'
  },
  'Meeting': {
    colorId: '7', // Teal
    description: 'Regulatory meetings'
  }
};

async function setEventColor(
  eventId: string,
  category: keyof typeof regulatoryColors
): Promise<void> {
  // This would use the Calendar API update method
  // Implementation depends on MCP tool availability
}
```

## Error Handling

| Error | Description | Resolution |
|-------|-------------|------------|
| `invalid_datetime` | Invalid date/time format | Use ISO 8601 format |
| `invalid_attendee` | Invalid email address | Verify attendee emails |
| `event_conflict` | Scheduling conflict | Resolve conflict or confirm override |
| `unauthorized` | Invalid access token | Refresh OAuth token |
| `quota_exceeded` | API quota exceeded | Implement rate limiting |

## Testing

### Test Cases

1. **Event Creation**: Verify each event type
2. **Recurrence Rules**: Test recurring patterns
3. **Event Query**: Test filtering and search
4. **Reminder Logic**: Test reminder timing
5. **Sync Tests**: Test Notion integration
6. **Error Scenarios**: Test all error cases
