# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/factory_test1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/factory_test1.proto',
  package='google.protobuf.python.internal',
  serialized_pb=_b('\n,google/protobuf/internal/factory_test1.proto\x12\x1fgoogle.protobuf.python.internal\"\xd5\x03\n\x0f\x46\x61\x63tory1Message\x12\x45\n\x0e\x66\x61\x63tory_1_enum\x18\x01 \x01(\x0e\x32-.google.protobuf.python.internal.Factory1Enum\x12\x62\n\x15nested_factory_1_enum\x18\x02 \x01(\x0e\x32\x43.google.protobuf.python.internal.Factory1Message.NestedFactory1Enum\x12h\n\x18nested_factory_1_message\x18\x03 \x01(\x0b\x32\x46.google.protobuf.python.internal.Factory1Message.NestedFactory1Message\x12\x14\n\x0cscalar_value\x18\x04 \x01(\x05\x12\x12\n\nlist_value\x18\x05 \x03(\t\x1a&\n\x15NestedFactory1Message\x12\r\n\x05value\x18\x01 \x01(\t\"P\n\x12NestedFactory1Enum\x12\x1c\n\x18NESTED_FACTORY_1_VALUE_0\x10\x00\x12\x1c\n\x18NESTED_FACTORY_1_VALUE_1\x10\x01*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02*<\n\x0c\x46\x61\x63tory1Enum\x12\x15\n\x11\x46\x41\x43TORY_1_VALUE_0\x10\x00\x12\x15\n\x11\x46\x41\x43TORY_1_VALUE_1\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FACTORY1ENUM = _descriptor.EnumDescriptor(
  name='Factory1Enum',
  full_name='google.protobuf.python.internal.Factory1Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FACTORY_1_VALUE_0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FACTORY_1_VALUE_1', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=553,
  serialized_end=613,
)
_sym_db.RegisterEnumDescriptor(_FACTORY1ENUM)

Factory1Enum = enum_type_wrapper.EnumTypeWrapper(_FACTORY1ENUM)
FACTORY_1_VALUE_0 = 0
FACTORY_1_VALUE_1 = 1


_FACTORY1MESSAGE_NESTEDFACTORY1ENUM = _descriptor.EnumDescriptor(
  name='NestedFactory1Enum',
  full_name='google.protobuf.python.internal.Factory1Message.NestedFactory1Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NESTED_FACTORY_1_VALUE_0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NESTED_FACTORY_1_VALUE_1', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=460,
  serialized_end=540,
)
_sym_db.RegisterEnumDescriptor(_FACTORY1MESSAGE_NESTEDFACTORY1ENUM)


_FACTORY1MESSAGE_NESTEDFACTORY1MESSAGE = _descriptor.Descriptor(
  name='NestedFactory1Message',
  full_name='google.protobuf.python.internal.Factory1Message.NestedFactory1Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.protobuf.python.internal.Factory1Message.NestedFactory1Message.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=458,
)

_FACTORY1MESSAGE = _descriptor.Descriptor(
  name='Factory1Message',
  full_name='google.protobuf.python.internal.Factory1Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='factory_1_enum', full_name='google.protobuf.python.internal.Factory1Message.factory_1_enum', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nested_factory_1_enum', full_name='google.protobuf.python.internal.Factory1Message.nested_factory_1_enum', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nested_factory_1_message', full_name='google.protobuf.python.internal.Factory1Message.nested_factory_1_message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scalar_value', full_name='google.protobuf.python.internal.Factory1Message.scalar_value', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list_value', full_name='google.protobuf.python.internal.Factory1Message.list_value', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FACTORY1MESSAGE_NESTEDFACTORY1MESSAGE, ],
  enum_types=[
    _FACTORY1MESSAGE_NESTEDFACTORY1ENUM,
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(1000, 536870912), ],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=551,
)

_FACTORY1MESSAGE_NESTEDFACTORY1MESSAGE.containing_type = _FACTORY1MESSAGE
_FACTORY1MESSAGE.fields_by_name['factory_1_enum'].enum_type = _FACTORY1ENUM
_FACTORY1MESSAGE.fields_by_name['nested_factory_1_enum'].enum_type = _FACTORY1MESSAGE_NESTEDFACTORY1ENUM
_FACTORY1MESSAGE.fields_by_name['nested_factory_1_message'].message_type = _FACTORY1MESSAGE_NESTEDFACTORY1MESSAGE
_FACTORY1MESSAGE_NESTEDFACTORY1ENUM.containing_type = _FACTORY1MESSAGE
DESCRIPTOR.message_types_by_name['Factory1Message'] = _FACTORY1MESSAGE
DESCRIPTOR.enum_types_by_name['Factory1Enum'] = _FACTORY1ENUM

Factory1Message = _reflection.GeneratedProtocolMessageType('Factory1Message', (_message.Message,), dict(

  NestedFactory1Message = _reflection.GeneratedProtocolMessageType('NestedFactory1Message', (_message.Message,), dict(
    DESCRIPTOR = _FACTORY1MESSAGE_NESTEDFACTORY1MESSAGE,
    __module__ = 'google.protobuf.internal.factory_test1_pb2'
    # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.Factory1Message.NestedFactory1Message)
    ))
  ,
  DESCRIPTOR = _FACTORY1MESSAGE,
  __module__ = 'google.protobuf.internal.factory_test1_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.Factory1Message)
  ))
_sym_db.RegisterMessage(Factory1Message)
_sym_db.RegisterMessage(Factory1Message.NestedFactory1Message)


# @@protoc_insertion_point(module_scope)
